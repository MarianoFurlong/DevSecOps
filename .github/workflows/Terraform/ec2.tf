data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "my_uwuntu" {
  ami           = "ami-0e83be366243f524a"
  instance_type = "t2.micro"
  key_name = "UwUntu"
  security_groups = [aws_security_group.my_security_group.id]
  subnet_id = "subnet-010d8909f140724b7"
  tags = {
    Name = "UwUntu"
  }
}
output "My_ip" {
  value = aws_instance.my_uwuntu.public_ip
}
resource "aws_security_group" "my_security_group" {
  name        = "my_security_group"
  description = "HTTP y SSH"
  vpc_id = "vpc-0dbd40414636b3867"

  ingress {
    description      = "HTTP from VPC"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  ingress {
    description      = "SSH from VPC"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
    ingress {
    description      = "HTTP from VPC"
    from_port        = 8080
    to_port          = 8080
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    }
    ingress {
    description      = "HTTP from VPC"
    from_port        = 9090
    to_port          = 9090
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    }    
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "allow_HTTP-SSH"
  }
}

