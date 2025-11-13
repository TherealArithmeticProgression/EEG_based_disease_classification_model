{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyODG4Y2s3p3ZweB1975nLE8"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 32,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UJwJxWn97VjN",
        "outputId": "bbe51a5e-ddb5-44f7-a145-a6c6ad6b2147"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Using Colab cache for faster access to the 'disorders-and-diagnosis-eeg-dataset-v3' dataset.\n",
            "A brief description of the data:                no.          age           IQ           EQ\n",
            "count  3444.000000  3444.000000  3444.000000  3444.000000\n",
            "mean   1722.500000    51.995935   114.256388   104.948316\n",
            "std     994.341491    19.802129    15.823531    32.047275\n",
            "min       1.000000    18.000000    87.000000    50.000000\n",
            "25%     861.750000    35.000000   101.000000    77.000000\n",
            "50%    1722.500000    52.000000   115.000000   105.000000\n",
            "75%    2583.250000    70.000000   128.000000   133.000000\n",
            "max    3444.000000    85.000000   141.000000   160.000000\n",
            "The first 5 rows:     no. sex  age    eeg.date    education   IQ   EQ   disorder/diagnosis  \\\n",
            "0    1   F   28  2024-10-31  High School  124   99            Parkinson   \n",
            "1    2   F   18  2024-06-07   University   98  108  Depressive disorder   \n",
            "2    3   M   59  2024-06-23  High School  123  157     Bipolar disorder   \n",
            "3    4   F   19  2024-06-20  High School   93  116          Psychopathy   \n",
            "4    5   F   29  2025-01-03   University  101   51                   MS   \n",
            "\n",
            "                                     EEG_Electrode_1  \\\n",
            "0  [0.33455714134489933, -1.0124825404627846, 0.4...   \n",
            "1  [-0.02739863367216427, -2.1875200427753687, -0...   \n",
            "2  [1.0050013043908792, 1.6817611285088891, -0.02...   \n",
            "3  [-0.43027103554325313, -0.9495404173994122, 0....   \n",
            "4  [1.5543439569608053, 2.2785650194030707, -3.20...   \n",
            "\n",
            "                                     EEG_Electrode_2  ...  \\\n",
            "0  [-0.49712810877710073, -1.181443147283427, -0....  ...   \n",
            "1  [-1.6063495702382038, -1.9489607776118076, -0....  ...   \n",
            "2  [-1.0385591774086103, 1.2250956787566445, 0.83...  ...   \n",
            "3  [-0.3237876606542493, 0.7128845452767104, 0.03...  ...   \n",
            "4  [-0.66726833185029, 0.7585408377070836, -0.303...  ...   \n",
            "\n",
            "                                    EEG_Electrode_23  \\\n",
            "0  [-1.99740458536635, 1.1675142221161818, -1.114...   \n",
            "1  [0.6887557986518217, -0.3765638799484069, 0.64...   \n",
            "2  [-1.1199358297465518, -1.850280760207885, 0.86...   \n",
            "3  [0.04156590423560202, 0.42027620630613444, 0.8...   \n",
            "4  [0.5264386679561065, -0.6702393228821288, 0.76...   \n",
            "\n",
            "                                    EEG_Electrode_24  \\\n",
            "0  [1.7731558286269427, -0.8660494297910852, 0.65...   \n",
            "1  [0.9580020402801734, 0.11347676004067732, -1.0...   \n",
            "2  [0.8814568522541026, 0.293235902200372, 0.3036...   \n",
            "3  [0.3055015728242051, 0.9390547474946099, 0.201...   \n",
            "4  [-0.07186336169811193, -0.9981504586508025, 0....   \n",
            "\n",
            "                                    EEG_Electrode_25  \\\n",
            "0  [-0.2391043711434249, -1.5441592677029112, -0....   \n",
            "1  [-0.5657130138418595, -0.4364533687176666, 0.0...   \n",
            "2  [1.7617998892464164, -0.2746956613556493, 1.65...   \n",
            "3  [0.5588089727285818, -0.17132871262269428, -0....   \n",
            "4  [-0.638747287207778, -0.6485048304469717, 1.98...   \n",
            "\n",
            "                                    EEG_Electrode_26  \\\n",
            "0  [0.1587242362378963, 0.7578533521985614, -1.46...   \n",
            "1  [-0.22115579682549202, 1.485179632951922, 0.43...   \n",
            "2  [-0.23674162770929155, -1.9493936103275236, -0...   \n",
            "3  [-1.983526303150428, -0.45274813775690154, 0.3...   \n",
            "4  [-1.4719549650034853, 0.838684896631107, 0.555...   \n",
            "\n",
            "                                    EEG_Electrode_27  \\\n",
            "0  [0.6316355991945747, -0.3678480270031867, -1.3...   \n",
            "1  [1.2361833741288593, -0.4357165426202037, 1.40...   \n",
            "2  [-0.7963995959246195, -0.15201814117080004, 1....   \n",
            "3  [0.5019664433487486, -0.8938051132944905, -1.2...   \n",
            "4  [0.6968676602358026, -0.3788571056047837, -0.0...   \n",
            "\n",
            "                                    EEG_Electrode_28  \\\n",
            "0  [-1.4444667012235493, 2.2621772753996514, -0.5...   \n",
            "1  [-0.3686085024420043, -0.10918331805000155, -0...   \n",
            "2  [-0.563035007550588, 0.16101140922425464, 0.07...   \n",
            "3  [1.458871854920239, 0.12823682600076106, 1.503...   \n",
            "4  [-1.4804857637591342, -2.3024773024616936, 1.3...   \n",
            "\n",
            "                                    EEG_Electrode_29  \\\n",
            "0  [0.15387878503907995, -0.10853770234891194, -0...   \n",
            "1  [0.2726137476493269, -0.008248258578368504, 1....   \n",
            "2  [0.5750813115048556, -0.3098870800966042, 0.75...   \n",
            "3  [-1.1090947792585244, -0.34756725922122883, -0...   \n",
            "4  [1.9173791176876227, -1.10512256096403, 1.2654...   \n",
            "\n",
            "                                    EEG_Electrode_30  \\\n",
            "0  [0.3154781284463222, 0.9463885574242941, 1.099...   \n",
            "1  [0.26342122129676815, 1.8219102244040832, -0.8...   \n",
            "2  [-0.2076793528753609, -0.24468906421486908, 0....   \n",
            "3  [-0.7097904204884279, -0.5647292673395053, 0.3...   \n",
            "4  [-0.5355393638751318, -0.3880278973261586, -1....   \n",
            "\n",
            "                                    EEG_Electrode_31  \\\n",
            "0  [0.5526415164712162, -0.2544903680359615, -2.0...   \n",
            "1  [-0.8784199632117726, -0.5760279509082266, 1.0...   \n",
            "2  [-0.856616999041279, 0.3935970670401432, 0.542...   \n",
            "3  [-0.03142591776844011, -1.677637114372979, -1....   \n",
            "4  [0.2294584405683268, 0.9123223629271447, -1.21...   \n",
            "\n",
            "                                    EEG_Electrode_32  \n",
            "0  [1.0021452006377516, 0.3729396954838123, -0.74...  \n",
            "1  [0.45690822319584296, -2.4112525822450555, -2....  \n",
            "2  [0.07681096961593926, 0.768816229114708, -0.59...  \n",
            "3  [0.5916353841295418, 0.7115851187328803, -0.57...  \n",
            "4  [-0.5800779808862577, 0.19416927087993818, -0....  \n",
            "\n",
            "[5 rows x 40 columns]\n"
          ]
        }
      ],
      "source": [
        "\n",
        "import kagglehub\n",
        "from kagglehub import KaggleDatasetAdapter\n",
        "import pandas as pd\n",
        "# Set the path to the file you'd like to load\n",
        "file_path = \"synthetic_eeg_data-v3.csv\"\n",
        "\n",
        "# Load the latest version\n",
        "df = kagglehub.dataset_load(\n",
        "  KaggleDatasetAdapter.PANDAS,\n",
        "  \"eyppler/disorders-and-diagnosis-eeg-dataset-v3\",\n",
        "  file_path)\n",
        "\n",
        "print(\"A brief description of the data:\", df.describe())\n",
        "print(\"The first 5 rows: \",df.head())"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Preprocessing\n",
        "df.isnull().sum()\n",
        "df_clean = df.dropna() #the dataset initially lacks empty fields\n",
        "\n"
      ],
      "metadata": {
        "id": "PEcZQsD584OL"
      },
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import LabelEncoder\n",
        "le_sex = LabelEncoder()\n",
        "df['sex'] = le_sex.fit_transform(df['sex']) # Pass a 1D array (Sex)\n",
        "le_disorder = LabelEncoder()\n",
        "df['disorder/diagnosis'] = le_disorder.fit_transform(df['disorder/diagnosis']) # Pass a 1D array (Diagnosis)\n",
        "le_education = LabelEncoder() # Add LabelEncoder for 'education'\n",
        "df['education'] = le_education.fit_transform(df['education']) # Added: Encode 'education' column"
      ],
      "metadata": {
        "id": "AZJYXQTEkdOn"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import ast\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "import pandas as pd # Ensure pandas is imported as it's used in the fix\n",
        "\n",
        "# Original numerical scalar features\n",
        "numerical_scalar_features = ['age', 'IQ', 'EQ']\n",
        "\n",
        "# EEG electrode column names (original list columns)\n",
        "eeg_cols = [f'EEG_Electrode_{i}' for i in range(1, 33)]\n",
        "\n",
        "# 1. Convert string representations of lists to actual lists for EEG_Electrode columns\n",
        "#    Using ast.literal_eval for safe evaluation of string literals\n",
        "for col in eeg_cols:\n",
        "    df[col] = df[col].apply(ast.literal_eval)\n",
        "\n",
        "# 2. Determine the length of the EEG electrode lists (assuming all are consistent)\n",
        "#    This is done by taking the first element of the first EEG column after conversion\n",
        "list_length = len(df[eeg_cols[0]].iloc[0])\n",
        "\n",
        "# 3. Create a list of new column names for the expanded EEG features\n",
        "new_eeg_feature_names = [f\"{eeg_col}_{j}\" for eeg_col in eeg_cols for j in range(list_length)]\n",
        "\n",
        "# 4. Create a temporary DataFrame for the expanded EEG features\n",
        "#    This converts each list in an EEG column into multiple new columns\n",
        "eeg_expanded_df_parts = []\n",
        "for col in eeg_cols:\n",
        "    eeg_expanded_df_parts.append(df[col].apply(pd.Series).add_prefix(f\"{col}_\"))\n",
        "\n",
        "df_eeg_expanded = pd.concat(eeg_expanded_df_parts, axis=1)\n",
        "\n",
        "# 5. Drop the original EEG columns from df\n",
        "df = df.drop(columns=eeg_cols)\n",
        "\n",
        "# 6. Concatenate the expanded EEG features back into df\n",
        "df = pd.concat([df, df_eeg_expanded], axis=1)\n",
        "\n",
        "# 7. Now, define the complete list of features to scale, including the newly expanded EEG features\n",
        "all_features_to_scale = numerical_scalar_features + new_eeg_feature_names\n",
        "\n",
        "# 8. Apply StandardScaler to the selected features in the modified df\n",
        "scaler = StandardScaler()\n",
        "df[all_features_to_scale] = scaler.fit_transform(df[all_features_to_scale])"
      ],
      "metadata": {
        "id": "CPwW0MdFnrf0"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#We're dividing the dataset in trial and testing data respectively\n",
        "\n",
        "from sklearn.model_selection import train_test_split\n",
        "remove = ['disorder/diagnosis','no.','eeg.date']\n",
        "X = df.drop(remove,axis=1)\n",
        "y = df['disorder/diagnosis']\n",
        "\n",
        "X_train,X_val,y_train,y_val = train_test_split(\n",
        "     X,y,test_size=0.2,random_state=42, stratify=y #to ensure that the proportion of data distributed across y has the same proportion\n",
        " )\n",
        "\n"
      ],
      "metadata": {
        "id": "MVN4rhZWHRr5"
      },
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#To build a flat multi class classifier using random forests module. A flat multiclass\n",
        "#classifier is anything that classifies the entity NOT on a heirarchial basis.\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.svm import SVC #for robustness against outliers\n",
        "from sklearn.neural_network import MLPClassifier\n",
        "#random forest\n",
        "rf_model=RandomForestClassifier(n_estimators=100, random_state=42)\n",
        "rf_model.fit(X_train,y_train)\n",
        "#support vector machine\n",
        "svm_model =SVC(kernel='rbf',random_state=42)\n",
        "svm_model.fit(X_train,y_train)\n",
        "#neural network\n",
        "nn_model=MLPClassifier(hidden_layer_sizes=(128,64),random_state=42)\n",
        "nn_model=(X_train,y_train)"
      ],
      "metadata": {
        "id": "JgoDjmi8IsUk"
      },
      "execution_count": 38,
      "outputs": []
    }
  ]
}
