variable "access" {
  type = object({
    region         = string
    access_key     = string
    secret_key     = string
    key_name       = string
    vpc_id = string
  })
  default = {
    region         = "value"
    access_key     = "value"
    secret_key     = "value"
    key_name       = "value"
    vpc_id = "value"
  }
}

variable "ansible" {
  type = object({
    public_key = string
  })
  default = {
    public_key = "value"
  }
}


variable "ec2_instances" {
  type = list(object({
    owner               = string
    platform            = string
    architecture        = string
    virtualization-type = string
    name                = string
    instance_type       = string
    tag                 = string
    security_group = string
  }))
  default = [
    {
      owner               = "value"
      platform            = "value"
      architecture        = "value"
      virtualization-type = "value"
      name                = "value"
      instance_type       = "value"
      tag                 = "value"
      security_group = "value"
    }
  ]
}
