def send_to_chatgpt(user_text: str) -> str:
    print("🤖 [chatgpt_api] Received text:")
    print(f"    {user_text}")
    response = "hello... until 50 tokens are written"
    print("🤖 [chatgpt_api] Responding with:")
    print(f"    {response}")
    return response
