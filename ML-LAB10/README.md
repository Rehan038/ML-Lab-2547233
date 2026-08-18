# Machine Learning Lab 10: Multi-Layer Perceptron (MLP) & Solving the Non-Linear XOR Problem

## 📌 Overview
This lab investigates the limitations of single-layer perceptrons on non-linearly separable problems and demonstrates how **Multi-Layer Perceptrons (MLPs)** solve the classic **XOR (Exclusive OR)** problem using hidden layer representations, non-linear activation functions, backpropagation, and gradient descent. Both high-level **Keras** and low-level **TensorFlow** implementations are built and analyzed.

---

## 🎯 Objectives
- **The XOR Challenge**:
  - Understand why single-layer linear perceptrons fail on the XOR truth table (Minsky & Papert, 1969) due to linear non-separability.
- **Keras Multi-Layer Perceptron Implementation**:
  - Construct a feedforward neural network (`Sequential`) with an input layer ($2$ inputs), hidden layer ($4$ or $8$ neurons with `ReLU` or `tanh` activation), and an output neuron (`sigmoid` activation).
  - Compile the network using `Adam` optimizer and `BinaryCrossentropy` loss:
    $$\mathcal{L}(y, \hat{y}) = - \left( y \log(\hat{y}) + (1-y) \log(1-\hat{y}) \right)$$
- **Low-Level TensorFlow Custom Implementation**:
  - Manually define trainable weight and bias tensors (`tf.Variable`).
  - Implement forward propagation, manual binary cross-entropy loss, and gradient computation with `tf.GradientTape()`.
  - Update parameters using custom gradient descent step equations.
- **Decision Boundary & Convergence Visualizations**:
  - Plot 2D non-linear decision boundary surfaces capturing the dual-hyperplane separation required for XOR.
  - Track loss reduction and accuracy progression across training epochs.
- **Hyperparameter & Learning Rate Experiments**:
  - Compare model behavior under varying learning rates ($\alpha = 0.05$ vs. $\alpha = 0.001$).
  - Analyze how insufficient learning rates or too few neurons can cause the model to get stuck in local plateaus.

---

## 📊 XOR Truth Table & Dataset
$$\begin{array}{|c|c|c|}
\hline
X_1 & X_2 & Y (X_1 \oplus X_2) \\
\hline
0 & 0 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 0 \\
\hline
\end{array}$$

---

## 🔬 Lab Architecture & Workflow

```
Input (x1, x2)
       │
       ▼
Hidden Layer (Dense + Non-Linear Activation [ReLU / tanh])
       │
       ▼
Output Layer (Dense 1 + Sigmoid Activation)
       │
       ▼
Predicted Probability ──► Binary Cross-Entropy Loss ──► Backpropagation (Adam / SGD)
```

| Component | High-Level Keras API | Low-Level TensorFlow (`tf.GradientTape`) |
| :--- | :--- | :--- |
| **Model Structure** | `tf.keras.Sequential([Dense(...), Dense(...)])` | `tf.Variable` weights ($W_1, b_1, W_2, b_2$) |
| **Forward Pass** | Built-in layer calls | `z1 = tf.matmul(X, W1) + b1; a1 = tf.nn.relu(z1)...` |
| **Loss Function** | `tf.keras.losses.BinaryCrossentropy()` | Custom vector formulation |
| **Optimization** | `model.compile(optimizer=Adam(lr), ...)` | `tape.gradient(loss, [W1, b1, W2, b2])` + custom step |
| **Decision Boundary** | Meshgrid prediction contour plot | Forward function meshgrid contour plot |

---

## 💡 Key Findings & Neural Network Insights
- **Linear Inseparability**: No single straight decision boundary can separate $(0,0)$ and $(1,1)$ from $(0,1)$ and $(1,0)$.
- **Hidden Layer Transformation**: Hidden neurons transform the 2D input space into an intermediate representation where the XOR classes become linearly separable.
- **Learning Rate Dynamics**:
  - With a tuned learning rate ($\alpha \approx 0.05$), the network achieves 100% classification accuracy in 30–50 epochs.
  - With small learning rates ($\alpha = 0.001$), optimization requires substantially more iterations to escape flat saddle regions.

---

## 🛠️ Requirements & Setup
```bash
pip install numpy matplotlib tensorflow
```
Open and run [`ML-LAB10.ipynb`](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB10/ML-LAB10.ipynb) in Jupyter Notebook or VS Code.
