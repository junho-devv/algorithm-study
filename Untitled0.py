{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMUDX2UUYuUhZFOWJPuuubo"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AynDVvPvQ3AK"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        },
        "id": "JaLISspvQOoz",
        "outputId": "62cc0cdf-43b4-413d-ff88-f611b751c5a2"
      },
      "source": [
        "import time\r\n",
        "\r\n",
        "start_time = time.time()\r\n",
        "\r\n",
        "array = [2, 3, 5, 7, 11]\r\n",
        "summary = 0\r\n",
        "\r\n",
        "for x in array:\r\n",
        "    summary += x\r\n",
        "\r\n",
        "end_time = time.time()\r\n",
        "\r\n",
        "print(summary)"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-5-e6ae919bacae>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0msummary\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msummary\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m\"고구마\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for +: 'int' and 'str'"
          ]
        }
      ]
    }
  ]
}