from getpass import getpass
import vk


APP_ID = 6406849


def get_user_login():
    return input('input login: ')


def get_user_password():
    return getpass('input password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, v=5.52)

    return api.users.get(
        user_ids=api.friends.getOnline(),
        fields='first_name, last_name'
    )


def output_friends_to_console(friends_online):
    print('\n Friends online:\n')
    for friend in friends_online:
        print('{} {}'.format(
            friend['first_name'],
            friend['last_name']
        ))


if __name__ == '__main__':
    try:
        login = get_user_login()
        password = get_user_password()
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        print('Incorrect login or password. Try again.')
