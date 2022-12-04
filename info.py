from instagramy import InstagramUser as insta

username = input("Enter user name")
target = insta(username)

print("Username :" ,target.username)
print("No. of followers:" ,target.number_of_followers)
print("No. of people following:" ,target.number_of_followings)
print("Posts :" ,target.number_of_posts)
print("Privacy Status :" ,target.is_private)
print("Verification :" ,target.is_verified)
