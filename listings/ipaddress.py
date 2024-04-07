from ip_location_pkg.findAddress import get_ip_location


def main():
    ip_location = get_ip_location()
    if ip_location:
        print(f"IP: {ip_location['ip']}, City: {ip_location['city']}, Region: {ip_location['region']}, Country: {ip_location['country']}")
    else:
        print("Failed to retrieve IP location.")

if __name__ == "__main__":
    main()
