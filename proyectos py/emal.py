email = input('cual es tu dirreccion de correo electronico: ').strip()

user_name = email[:email.index("@")]

domain_name = email[email.index("@")+1]

output = "Your username in '{}' and your domain is '{}' ".format(user_name,domain_name)

print(output)