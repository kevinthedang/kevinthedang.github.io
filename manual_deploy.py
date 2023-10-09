import os

# setup
print("\nPreparing Deployment...\n")
command = "npm run deploy -- -m "

# require deployment message
commit_message = input("Provide Deployment Message: ")

# print result
print("Received Commit Message was:", commit_message)

# attempt to deploy
print("\nDeploying...")
os.system(command + commit_message)

# end
print("\nFinished Deployment...\n")