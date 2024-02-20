terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.37.0"
    }
  }

  required_version = ">= v1.7.3"
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

module "secrets" {
  source = "./modules/terraform-aws-secretsmanager"
}
