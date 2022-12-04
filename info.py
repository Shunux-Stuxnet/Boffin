from instagramy import InstagramUser as insta

username = input("Enter user name")
target = insta(username)

print("Username :" ,target.username)
print("No. of followers:" ,target.number_of_followers)
print("No. of people following:" ,target.number_of_followings)
print("Posts :" ,target.number_of_posts)
print("Privacy Status :" ,target.is_private)
print("Verification :" ,target.is_verified)



# import the modules
import instagram_explore as ie
import json
  
# search user name
result = ie.user('timesofindia')
  
parsed_data= json.dumps(result, indent = 4,
                        sort_keys = True)
  
# displaying the data
print(parsed_data[15:400])
