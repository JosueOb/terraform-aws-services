# System credentials
resource "aws_secretsmanager_secret" "system_credentials" {
  name = "system_credentials"
}
resource "aws_secretsmanager_secret_version" "system_credentials" {
  secret_id     = aws_secretsmanager_secret.system_credentials.id
  secret_string = jsonencode(var.system_credentials)
}

# Connection credentials
resource "aws_secretsmanager_secret" "connection_credentials" {
  name = "connection_credentials"
}
resource "aws_secretsmanager_secret_version" "connection_credentials" {
  secret_id     = aws_secretsmanager_secret.connection_credentials.id
  secret_string = jsonencode(var.connection_credentials)
}
