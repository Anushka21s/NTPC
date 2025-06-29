{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "741c5851-8bf3-4d0e-8929-d268feca837d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\satis\\AppData\\Local\\Temp\\ipykernel_47124\\3166352319.py:22: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  X['Source'] = le_source.fit_transform(X['Source'])\n",
      "C:\\Users\\satis\\AppData\\Local\\Temp\\ipykernel_47124\\3166352319.py:23: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  X['Siding'] = le_siding.fit_transform(X['Siding'])\n",
      "C:\\Users\\satis\\AppData\\Local\\Temp\\ipykernel_47124\\3166352319.py:24: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  X['Invoice Grade'] = le_invoice.fit_transform(X['Invoice Grade'])\n",
      "C:\\Users\\satis\\miniconda3\\Lib\\site-packages\\sklearn\\metrics\\_classification.py:1531: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n",
      "C:\\Users\\satis\\miniconda3\\Lib\\site-packages\\sklearn\\metrics\\_classification.py:1531: UndefinedMetricWarning: Recall is ill-defined and being set to 0.0 in labels with no true samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n",
      "C:\\Users\\satis\\miniconda3\\Lib\\site-packages\\sklearn\\metrics\\_classification.py:1531: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n",
      "C:\\Users\\satis\\miniconda3\\Lib\\site-packages\\sklearn\\metrics\\_classification.py:1531: UndefinedMetricWarning: Recall is ill-defined and being set to 0.0 in labels with no true samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n",
      "C:\\Users\\satis\\miniconda3\\Lib\\site-packages\\sklearn\\metrics\\_classification.py:1531: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n",
      "C:\\Users\\satis\\miniconda3\\Lib\\site-packages\\sklearn\\metrics\\_classification.py:1531: UndefinedMetricWarning: Recall is ill-defined and being set to 0.0 in labels with no true samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.2440087145969499\n",
      "Classification report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "           0       0.00      0.00      0.00         0\n",
      "           1       0.00      0.00      0.00         1\n",
      "           2       0.00      0.00      0.00         2\n",
      "           3       0.25      1.00      0.40         1\n",
      "           4       1.00      1.00      1.00         1\n",
      "           5       0.00      0.00      0.00         9\n",
      "           6       0.36      0.17      0.23        24\n",
      "           7       0.21      0.13      0.16        53\n",
      "           8       0.28      0.34      0.31        92\n",
      "           9       0.24      0.43      0.31        75\n",
      "          10       0.18      0.11      0.13        75\n",
      "          11       0.24      0.36      0.29        55\n",
      "          12       0.24      0.14      0.18        50\n",
      "          13       0.25      0.05      0.08        21\n",
      "\n",
      "    accuracy                           0.24       459\n",
      "   macro avg       0.23      0.27      0.22       459\n",
      "weighted avg       0.24      0.24      0.22       459\n",
      "\n",
      "Possible Sources: ['ECL', 'IMP-ADEL', 'IMP-ADI', 'MCL', 'MCL ', 'NCL', 'NCL-RCR-Aakar', 'NCL-RCR-KSR', 'NCL-RCR-Omax', 'NLC-RCR', 'PAKRI', 'SCCL', 'SCCL-RCR', 'SECL', 'SECL-RCR-ACB', 'WCL', 'WCL ', 'WCL-RCR', 'WCL-RCR (KUM+INDO)', 'WCL-RCR (PTC+INDO)', 'WCL-RCR PTC', 'WCL-RCR PTC & KSR', 'WCL-RCR-INDO', 'WCL-RCR-KSR & KOH']\n",
      "Possible Sidings: ['ACTR', 'AKPK', 'BBMT', 'BCDL', 'BCMT', 'BNDG', 'BNDG\\xa0', 'BOCB', 'BOCM', 'BOMB', 'BOMK', 'BRRB', 'BWWL', 'CGM', 'CSPS', 'DKSK', 'DKSK\\xa0', 'DWWS', 'GCNM', 'GGPP', 'GGS', 'GGS\\xa0', 'GICK', 'GOSG', 'GPCK', 'GSG', 'GWCB', 'GXSG', 'JCZ', 'JNCN', 'JRGR', 'JVRB', 'KCKT', 'KMKA', 'KSCK', 'LOCM', 'LOMB', 'LOMB\\xa0', 'LSST', 'LTC', 'MAIL', 'MBCB', 'MCFL', 'MCLK', 'MCSP', 'MFSJ', 'MSCA', 'MUGR', 'NCSN', 'NKCR', 'NMCL', 'NWSN', 'OKSR', 'PMCS', 'POCP', 'PRPI', 'PSBP', 'PSCE', 'PSEC', 'PVIT', 'RGPM', 'RUSG', 'SBCT', 'SCDG', 'SCRM', 'SCU', 'SLCC', 'SOCM', 'SPSG', 'SSAP', 'SSMN', 'UMSG', 'VWLR', 'WANI']\n",
      "Possible Invoice Grades: ['G03', 'G04', 'G05', 'G06', 'G07', 'G08', 'G09', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'WC1']\n",
      "\n",
      "--- Predict Unloading Grade ---\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Source (or 'exit' to quit):  WCL\n",
      "Enter Siding:  MBCB\n",
      "Enter Invoice Grade:  G07\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\satis\\miniconda3\\Lib\\site-packages\\sklearn\\base.py:493: UserWarning: X does not have valid feature names, but RandomForestClassifier was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Predicted Unloading Grade: G12\n",
      "\n",
      "--- Predict Unloading Grade ---\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Source (or 'exit' to quit):  EXIT\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Program ended.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.metrics import classification_report, accuracy_score\n",
    "\n",
    "# 1. Load and clean the data\n",
    "file_path = 'final 2.xlsx'\n",
    "df = pd.read_excel(file_path, header=1)\n",
    "df = df.dropna()\n",
    "\n",
    "# 2. Select features and target\n",
    "X = df[['Source', 'Siding', 'Invoice Grade']]\n",
    "y = df['Unloading Grade']\n",
    "\n",
    "# 3. Encode categorical features and target\n",
    "le_source = LabelEncoder()\n",
    "le_siding = LabelEncoder()\n",
    "le_invoice = LabelEncoder()\n",
    "le_unloading = LabelEncoder()\n",
    "\n",
    "X['Source'] = le_source.fit_transform(X['Source'])\n",
    "X['Siding'] = le_siding.fit_transform(X['Siding'])\n",
    "X['Invoice Grade'] = le_invoice.fit_transform(X['Invoice Grade'])\n",
    "y = le_unloading.fit_transform(y)\n",
    "\n",
    "# 4. Split data into train/test\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# 5. Build and train the model\n",
    "model = RandomForestClassifier(random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# 6. Evaluate the model\n",
    "y_pred = model.predict(X_test)\n",
    "print(\"Accuracy:\", accuracy_score(y_test, y_pred))\n",
    "print(\"Classification report:\\n\", classification_report(y_test, y_pred))\n",
    "\n",
    "# 7. List possible values for interactive input\n",
    "print(\"Possible Sources:\", list(le_source.classes_))\n",
    "print(\"Possible Sidings:\", list(le_siding.classes_))\n",
    "print(\"Possible Invoice Grades:\", list(le_invoice.classes_))\n",
    "\n",
    "# 8. Interactive prediction loop\n",
    "while True:\n",
    "    print(\"\\n--- Predict Unloading Grade ---\")\n",
    "    source = input(\"Enter Source (or 'exit' to quit): \")\n",
    "    if source.lower() == 'exit':\n",
    "        break\n",
    "    siding = input(\"Enter Siding: \")\n",
    "    invoice_grade = input(\"Enter Invoice Grade: \")\n",
    "    try:\n",
    "        source_enc = le_source.transform([source])\n",
    "        siding_enc = le_siding.transform([siding])\n",
    "        invoice_enc = le_invoice.transform([invoice_grade])\n",
    "        X_new = [[source_enc[0], siding_enc[0], invoice_enc[0]]]\n",
    "        pred = model.predict(X_new)\n",
    "        unloading_grade = le_unloading.inverse_transform(pred)\n",
    "        print(f\"Predicted Unloading Grade: {unloading_grade[0]}\")\n",
    "    except ValueError as e:\n",
    "        print(\"Invalid input! Please enter values exactly as shown in the possible values.\")\n",
    "\n",
    "print(\"Program ended.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a5c1f938-0f61-4308-a36f-1a8695809f42",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\satis\\AppData\\Local\\Temp\\ipykernel_58788\\859620375.py:19: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  X['Source'] = le_source.fit_transform(X['Source'])\n",
      "C:\\Users\\satis\\AppData\\Local\\Temp\\ipykernel_58788\\859620375.py:20: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  X['Siding'] = le_siding.fit_transform(X['Siding'])\n",
      "C:\\Users\\satis\\AppData\\Local\\Temp\\ipykernel_58788\\859620375.py:21: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  X['Invoice Grade'] = le_invoice.fit_transform(X['Invoice Grade'])\n",
      "2025-06-07 08:19:00.617 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.617 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.624 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.625 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.626 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.626 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.626 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.628 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.628 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.628 `label` got an empty value. This is discouraged for accessibility reasons and may be disallowed in the future by raising an exception. Please provide a non-empty label and hide it with label_visibility if needed.\n",
      "2025-06-07 08:19:00.631 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.637 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.639 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.643 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.645 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.645 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.645 `label` got an empty value. This is discouraged for accessibility reasons and may be disallowed in the future by raising an exception. Please provide a non-empty label and hide it with label_visibility if needed.\n",
      "2025-06-07 08:19:00.649 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.653 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.654 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.655 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.655 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.655 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.655 `label` got an empty value. This is discouraged for accessibility reasons and may be disallowed in the future by raising an exception. Please provide a non-empty label and hide it with label_visibility if needed.\n",
      "2025-06-07 08:19:00.658 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.658 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.660 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.660 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.662 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.663 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.663 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.665 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-07 08:19:00.665 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "# Load and prepare data\n",
    "file_path = 'final 2.xlsx'\n",
    "df = pd.read_excel(file_path, header=1)\n",
    "df = df.dropna()\n",
    "X = df[['Source', 'Siding', 'Invoice Grade']]\n",
    "y = df['Unloading Grade']\n",
    "\n",
    "# Encode categories\n",
    "le_source = LabelEncoder()\n",
    "le_siding = LabelEncoder()\n",
    "le_invoice = LabelEncoder()\n",
    "le_unloading = LabelEncoder()\n",
    "X['Source'] = le_source.fit_transform(X['Source'])\n",
    "X['Siding'] = le_siding.fit_transform(X['Siding'])\n",
    "X['Invoice Grade'] = le_invoice.fit_transform(X['Invoice Grade'])\n",
    "y = le_unloading.fit_transform(y)\n",
    "\n",
    "# Model\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "model = RandomForestClassifier(random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# --- WEB PAGE LAYOUT ---\n",
    "st.set_page_config(page_title=\"Unloading Grade Predictor\", layout=\"centered\")\n",
    "\n",
    "# Centered title only\n",
    "st.markdown(\"<h2 style='text-align: center;'>Unloading Grade Predictor</h2>\", unsafe_allow_html=True)\n",
    "\n",
    "# Only dropdowns and a button (no extra info)\n",
    "col1, col2, col3 = st.columns(3)\n",
    "\n",
    "with col1:\n",
    "    source = st.selectbox(\"\", options=le_source.classes_, key=\"source\")\n",
    "with col2:\n",
    "    siding = st.selectbox(\"\", options=le_siding.classes_, key=\"siding\")\n",
    "with col3:\n",
    "    invoice_grade = st.selectbox(\"\", options=le_invoice.classes_, key=\"invoice_grade\")\n",
    "\n",
    "predict_button = st.button(\"Predict\")\n",
    "\n",
    "if predict_button:\n",
    "    source_enc = le_source.transform([source])\n",
    "    siding_enc = le_siding.transform([siding])\n",
    "    invoice_enc = le_invoice.transform([invoice_grade])\n",
    "    X_new = [[source_enc[0], siding_enc[0], invoice_enc[0]]]\n",
    "    pred = model.predict(X_new)\n",
    "    unloading_grade = le_unloading.inverse_transform(pred)\n",
    "    st.markdown(f\"<h3 style='text-align: center; color: green;'>Predicted Unloading Grade: {unloading_grade[0]}</h3>\", unsafe_allow_html=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "76c8ecac-8951-4390-a3ec-da0a38d9a07e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
