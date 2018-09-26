# Salarium Proof of Concept - RDS, DynamoDB, SAM

We are using AWS Cloudformation to deploy Infrastructure as a Code (IaC) needed for RDS, DynamoDB and Lambda(SAM) deployment.

## Pre-Requisites

We use [AWS Command Line Interface](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) and [Serverless Application Model(SAM) CLI](https://docs.aws.amazon.com/lambda/latest/dg/sam-cli-requirements.html) to run steps below.

Please follow [instructions](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) if you haven't installed AWS CLI. Your CLI [configuration](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) need PowerUserAccess and IAMFullAccess [IAM policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) associated with your credentials

```console
aws --version
```

Output from above must yield **AWS CLI version >= 1.11.37**

Please follow [instructions](https://docs.aws.amazon.com/lambda/latest/dg/sam-cli-requirements.html) if you haven't installed SAM CLI.

```console
sam --version
```

Output from above must yield **SAM CLI, version >= 0.5.0**

## Quick setup

#### 1. Clone this repo

```console
git clone https://github.com/vivifyideas/salarium-poc-rdb-dynamodb-lambda
```

#### 2. Run bin/deploy

```console
bin/deploy
```

## RDS deploy details

Here are the inputs required to launch RDS CloudFormation template:

- **Database Name**: Enter name for database that will be created
- **Database Admin username**: Enter username for newely created db admin user
- **Database Admin Password**: Enter password for newely created db admin user
- **CloudFormation Stack Name**: Enter CloudFormation Stack Name to create stack

## DynamoDB Table deploy details

Here are the inputs required to launch DynamoDB CloudFormation template:

- **Table Name**: Enter name for table that will be created
- **HashType PrimaryKey Name**: Enter HashType PrimaryKey Name for table
- **HashType PrimaryKey Type**: Enter HashType PrimaryKey Type for table
- **Provisioned read throughput**: Enter Provisioned read throughput, defaults to 5
- **Provisioned write throughput**: Enter Provisioned write throughput, defaults to 10
- **CloudFormation Stack Name**: Enter CloudFormation Stack Name to create stack

## SAM(Lambda) deploy details

Here are the inputs required to launch SAM(Lambda) CloudFormation template:

- **S3 Bucket**: Enter S3 Bucket for storing your CloudFormation template and lambdas.
- **CloudFormation Stack Name**: Enter CloudFormation Stack Name to create stacks

## Cleanup

Just delete CloudFormation stacks, this will delete all created resources.
