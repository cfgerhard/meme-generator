import argparse

if  __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Say a Greeting.')
    parser.add_argument('name', help='Name to greet')
    parser.add_argument('--city',  help='City where Name is living', default="Hannover")
    name = parser.parse_args().name
    city = parser.parse_args().city

    # Alternatively first get the arguments and then define the variables
    # args = parser.parse_args()
    # name = args.name
    # city = args.city

    print(f'Hello, {name} from {city}')
