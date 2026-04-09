# 📊 E-commerce Sales Analysis

End-to-end data analysis project using Python and Pandas to extract business insights from simulated e-commerce sales data.

---

## 🎯 Objective

The goal of this project is to analyze sales data and extract meaningful insights that could support business decisions, such as identifying top-performing products, sellers, and customers, as well as understanding sales trends over time.

---

## 🛠 Technologies

* Python
* Pandas
* Matplotlib

---

## 📊 Dataset

The dataset contains simulated e-commerce sales data, including:

* Sale ID
* Date
* Product
* Customer
* Seller
* Price
* Quantity

---

## 🔥 Key Insights

* 💰 **Total Revenue:** R$ 80,860
* 🖱 **Best-selling Product:** Mouse (77 units sold)
* 🧑‍💼 **Top Seller:** Ana (R$ 33,530 in sales)
* 🛍 **Top Customer:** Cliente_7 (R$ 10,820 in purchases)
* 📈 **Peak Sales Month:** February
* 📉 Sales showed a decline after February, with a significant drop in April

---

## 📈 Visualization

The project includes a bar chart that displays total sales per month, allowing clear visualization of trends and performance over time.

---

## 🧱 Project Structure

```
analise-vendas-ecommerce/
│
├── data/
│   ├── raw/
│   │   └── vendas.csv
│   └── processed/
│       └── vendas_tratadas.csv
│
├── src/
│   ├── gerar_dados.py
│   ├── limpar_dados.py
│   └── analise.py
│
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

1. Generate or use the dataset
2. Run data cleaning:

```
python src/limpar_dados.py
```

3. Run analysis:

```
python src/analise.py
```

---

## 🚀 About the Project

This project demonstrates the full data analysis workflow:

* Data generation
* Data cleaning and transformation
* Exploratory data analysis
* Business insights extraction
* Data visualization

---
## 📂 Dataset

The dataset used in this project is not included in the repository due to its size.

You can download it from the official Olist dataset:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

After downloading, place the files inside:

data/raw/

## 👨‍💻 Author

Developed by João Louzada
