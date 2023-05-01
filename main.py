from service.client import Service


def main():
    service = Service()
    # service.read_from_file('db.json')
    service.update_from_site()
    service.write_to_file('db.json')
    if __name__ == "__main__":
        main()
