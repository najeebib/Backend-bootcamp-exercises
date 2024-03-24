from modules.social_media import SocialMediaPlatform
from modules.improved_social_media import ImprovedSocialMediaPlatform
import time
def measure_time(platform: SocialMediaPlatform):
    num_of_measurements = 3
    measurements = {"register": [],"get_suer": [], "generate": []}
    
    for _ in range(num_of_measurements):
        start = time.perf_counter()
        platform.register_user("user")
        end = time.perf_counter()
        total =  end - start
        measurements["register"].append(total)
    
    for _ in range(num_of_measurements):
        start = time.perf_counter()
        user = platform.get_user_by_username("user")
        end = time.perf_counter()
        total =  end - start
        measurements["get_suer"].append(total)

    platform.register_user("user2")
    user2 = platform.get_user_by_username("user2")
    user2_post = user2.post_message("test msg")
    platform.add_post(user2_post)
    user.follow(user2.username)

    for _ in range(num_of_measurements):
        start = time.perf_counter()
        user = platform.generate_timeline("user")
        end = time.perf_counter()
        total =  end - start
        measurements["generate"].append(total)
    
        
    with open("performance_results.txt", 'a+') as f:
        if type(platform) == SocialMediaPlatform:
            f.write("Measurments for regular social media platform\n")
        else:
            f.write("Measurments for improved social media platform\n")
        for func_name, times in measurements.items():
            avg_time = sum(times) / num_of_measurements
            f.write(f"{func_name}: {avg_time} seconds\n")
        f.write("\n\n")
def main():
    f = open("performance_results.txt", 'w')
    f.close()
    """ measure the performance of the functions """
    

    platform = SocialMediaPlatform()
    measure_time(platform=platform)

    improved_platform = ImprovedSocialMediaPlatform()
    measure_time(platform=improved_platform)
    


if __name__ == "__main__":
    main()