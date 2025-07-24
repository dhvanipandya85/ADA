import numpy as np
from sklearn.linear_model import LinearRegression

def learning_component():
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])
    model = LinearRegression()
    model.fit(X, y)
    prediction = model.predict([[6]])
    print("1. Learning Component:")
    print("   Trained Linear Regression: Predict(6) =", prediction[0])

def reasoning_component():
    temperature = 38
    cough = True
    print("\n2. Reasoning Component:")
    if temperature > 37 and cough:
        print("   Rule matched: You may have a fever.")
    else:
        print("   Rule not matched.")

def problem_solving_component():
    maze = [
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 1],
        [1, 1, 0, 0]
    ]
    visited = set()
    path = []

    def dfs(x, y):
        if (x, y) in visited or not (0 <= x < 4 and 0 <= y < 4) or maze[x][y] == 1:
            return False
        path.append((x, y))
        visited.add((x, y))
        if (x, y) == (3, 3):
            return True
        if dfs(x+1, y) or dfs(x, y+1) or dfs(x-1, y) or dfs(x, y-1):
            return True
        path.pop()
        return False

    dfs(0, 0)
    print("\n3. Problem Solving Component:")
    print("   Path to exit:", path)

def perception_component():
    image_file = "image_cat.jpg"
    if "cat" in image_file:
        print("\n4. Perception Component:")
        print("   Detected: This is an image of a cat.")
    else:
        print("\n4. Perception Component:")
        print("   Unable to identify the object.")

def nlp_component():
    user_input = "What is AI?"
    response = ""
    if "ai" in user_input.lower():
        response = "AI stands for Artificial Intelligence."
    elif "hello" in user_input.lower():
        response = "Hello! How can I help you?"
    else:
        response = "Sorry, I don't understand."
    print("\n5. NLP Component:")
    print("   User:", user_input)
    print("   Bot:", response)

def main():
    print("==== AI Components Demonstration ====")
    learning_component()
    reasoning_component()
    problem_solving_component()
    perception_component()
    nlp_component()

if __name__ == "__main__":
    main()
