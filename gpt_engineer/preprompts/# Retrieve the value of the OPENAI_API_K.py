# Retrieve the value of the OPENAI_API_KEY environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the environment variable is set
if openai_api_key is None:
    print("The OPENAI_API_KEY environment variable is not set.")
else:
    print("The value of OPENAI_API_KEY is:", openai_api_key)
