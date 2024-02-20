# System credentials
variable "system_credentials" {
  description = "System Credentials"
  type        = map(string)
  default = {
    user     = "Test User"
    password = "Test Password 123"
  }
}

# Connection credentials
variable "connection_credentials" {
  description = "Connection Credentials"
  type        = map(string)
  default = {
    url   = "http://test-url.com"
    key   = "Test Connection Key"
    token = "Test Connection Token"
  }
}