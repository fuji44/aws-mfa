import sys, click, subprocess, json

@click.command()
@click.option('--account', '-a', required = True, help = 'AWS Account ID.')
@click.option('--user', '-u', required = True, help = 'AWS IAM User name.')
@click.option('--token', '-t', required = True, help = 'MFA Token.')
@click.option('--region', '-r', help = 'Target region.')
@click.option('--profile', '-p', help = 'Use awscli profile.')
def aws_mfa(account, user, token, region, profile):
    """
    Create a temporary profile to access AWS resources using MFA.

    example:

      aws-mfa --account <your AWS account ID> --user <your user name> --token <MFA token>
    """
    arn = "arn:aws:iam::" + account + ":mfa/" + user
    cmd = ["aws", "sts", "get-session-token", "--serial-number", arn, "--token-code", token]
    if not profile is None:
        cmd.extend(["--profile", profile])

    try:
        completed_process = subprocess.run(cmd, stdout = subprocess.PIPE, check = True)
        session_token_json = json.loads(completed_process.stdout)
    except subprocess.CalledProcessError as e:
        sys.exit(1)
    except ValueError:
        sys.stdout.write("No JSON object could be decoded")
        sys.exit(1)

    temp_profile = 'tmp-' + account + '-' + user
    set_aws_config("aws_access_key_id", session_token_json["Credentials"]["AccessKeyId"], temp_profile)
    set_aws_config("aws_secret_access_key", session_token_json["Credentials"]["SecretAccessKey"], temp_profile)
    set_aws_config("aws_session_token", session_token_json["Credentials"]["SessionToken"], temp_profile)
    if not region is None:
        set_aws_config("region", region, temp_profile)

    print("Successfully saved aws credential as profile " + temp_profile)
    print("Expiration: " + session_token_json["Credentials"]["Expiration"])
    print("Try it. aws s3 ls --profile " + temp_profile)

def set_aws_config(key, value, profile):
    cmd = ["aws", "configure", "set", key, value, "--profile=" + profile]
    subprocess.run(cmd)
