# Problem 12

def find_lost_socks_from_file(file_name):
    sock_count = {}  
    try:
        with open('input12.txt', 'r') as file:
            for line in file:
                sock = line.strip()  
                if sock == "END END END":  
                    break
                
                if sock in sock_count:
                    sock_count[sock] += 1
                else:
                    sock_count[sock] = 1

        lost_socks_found = False

        for sock, count in sock_count.items():
            if count % 2 != 0:  
                print(sock)
                lost_socks_found = True
    

        if not lost_socks_found:
            print("No lost socks")
        print(sock_count)
    except Exception as e:
        print(f"Error reading file: {e}")

find_lost_socks_from_file('input12.txt')
