print('\n'.join(list(filter(lambda x: x[0].lower() != 'v' or x[0] == '*',
                            input().split('; ')))).replace('*', ''))