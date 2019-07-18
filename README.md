# aws-mfa

A CLI tool that allows you to create temporary authentication profiles using MFA tokens.

## Usage

Install using pip.

```
pip install git+https://github.com/fuji44/aws-mfa.git
```

Once installed, you should be able to use the `aws-mfa` command.
Run `aws configure` to create credentials before running.

```
aws-mfa
```

To use a non-default profile for authentication, specify the `--profile` option.

```
aws-mfa --profile <profile_name>
```

It is usually run interactively.

```
$ aws-mfa
Account ID: <account_id>
IAM User name [fuji44]: <user_name>
MFA Token code: <token_code>
```

It can be executed non-interactively by specifying an option.

```
aws-mfa --account <account_id> --user <user_name> --token <token_code>
```

If successful, a profile with a temporary access key is created.
You can use it by specifying a profile with the AWS-CLI tool.

For example, to display the bucket of S3:
```
aws s3 ls --profile <temp profile>
```

## Known issues

On Windows, executing the aws command subprocess fails.
However, if run on WSL, it works fine.

## Reference

https://aws.amazon.com/premiumsupport/knowledge-center/authenticate-mfa-cli/
