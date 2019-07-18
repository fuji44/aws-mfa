# aws-mfa

## Usage

Install using pip.

```
pip install git+https://github.com/fuji44/aws-mfa.git
```

Run `aws configure` to create credentials before running.

Execute with arguments.

```
aws-mfa --account <account_id> --user <user_name> --token <token_code>
```

If successful, a profile with a temporary access key is created.
You can use it by specifying a profile with the AWS-CLI tool.

For example, to display the bucket of S3:
```
aws s3 ls --profile <temp profile>
```
