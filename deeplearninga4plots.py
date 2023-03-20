import numpy as np
import matplotlib.pyplot as plt

# define data points
X = np.array([[1, 1],
              [1, 0],
              [0, 1],
              [-1, -1],
              [-1, 0],
              [-1, 1]])
y = np.array([1, 1, 0, 0, 0, 0])

# define activation function (step function)
def step(x):
    return np.where(x >= 0, 1, 0)

# define gradient descent function
def gradient_descent(X, y, lr, epochs):
    w = np.array([1, 1]) # initial weights
    losses = [] # to store loss values
    for epoch in range(epochs):
        y_pred = step(np.dot(X, w)) # predicted labels
        error = y - y_pred
        loss = np.mean(error**2)
        losses.append(loss)
        w = w.astype('int64') + lr * np.dot(X.T, error).astype('int64')
        w += lr * np.dot(X.T, error) # update weights
    return w, losses

# train the model for 3 epochs with lr = 0.1
w, losses = gradient_descent(X, y, lr=0.1, epochs=3)
print('Trained weights:', w)

# plot learning curve
plt.plot(range(1, 4), losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Learning Curve')
plt.show()

# define the classifier derived in the last epoch
def predict(x):
    return np.where(np.dot(x, w) >= 0, 1, 0)

# plot data points
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Data Points')
plt.show()

# plot classifier line
x1 = np.linspace(-2, 2)
x2 = -(w[0]*x1) / w[1]
plt.plot(x1, x2)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Classifier')
plt.show()

# calculate confusion matrix, accuracy, sensitivity, and specificity
y_pred = predict(X)
tp = np.sum(np.logical_and(y_pred == 1, y == 1))
tn = np.sum(np.logical_and(y_pred == 0, y == 0))
fp = np.sum(np.logical_and(y_pred == 1, y == 0))
fn = np.sum(np.logical_and(y_pred == 0, y == 1))
conf_matrix = np.array([[tn, fp], [fn, tp]])
accuracy = (tp + tn) / len(y)
sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)
print('Confusion Matrix:\n', conf_matrix)
print('Accuracy:', accuracy)
print('Sensitivity:', sensitivity)
print('Specificity:', specificity)
