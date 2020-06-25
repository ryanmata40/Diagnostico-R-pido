def cadastrar():
    email = input("E-mail: ")
    name = input("Nome:")
    password = input("Senha: ")
    #adiciona user no arquivo de login
    f = open("logins.txt","r")
    content = f.readlines()
    content.append(email + ',' + name + ',' + password + '\n')
    f.close()
    f = open("logins.txt","w")
    f.writelines(content)
    f.close()

    #coleta lista de usuarios 'list_users'
    list_users = set()
    f = open("logins.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        contents = contents.splitlines()
        for content in contents:
            list_users.add(content)
    f.close()

    #testa se um usuario existe
    name_check = 'rafael2'
    for user in list_users:
      name_user = user.split(',')[0]
      if(name_user == name_check):
        print('usuario existe')

    print(list_users)

