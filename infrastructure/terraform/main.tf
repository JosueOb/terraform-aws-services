variable "localstack_endpoint" {
  description = "localstack endpoint"
  type        = string
  default     = "http://localstack:4566"
}

# Provider configuration https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/custom-service-endpoints#localstack
provider "aws" {
  region                      = "us-east-1"
  skip_requesting_account_id  = true
  skip_credentials_validation = true
  endpoints {
    secretsmanager = var.localstack_endpoint
  }
}

resource "aws_secretsmanager_secret" "system_credentials" {
  name = "system_credentials"
}

resource "aws_secretsmanager_secret_version" "system_credentials" {
  secret_id     = aws_secretsmanager_secret.system_credentials.id
  secret_string = "this is a test secret"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.37.0"
    }
  }

  required_version = ">= v1.7.3"
}