# Conceptual LLM demo
def explain_result(prediction):
    return f"AI Assistant would explain: The scan result is {prediction}."

if __name__ == "__main__":
    pred = "Normal"
    print(explain_result(pred))
