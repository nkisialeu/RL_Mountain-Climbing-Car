# Обучение с подкреплением: Подъем на гору [RU]

## Обзор

Этот проект направлен на обучение агента по обучению с подкреплением успешному навигации и подъему на виртуальную гору с использованием глубоких Q-сетей (DQN). Агент обучается с помощью обучения с подкреплением, используя память воспроизведения для хранения своих опытов и улучшения принятия решений со временем.

## Структура проекта

- **Agent**: Реализует основную логику выбора действий и обучения DQN.
- **QNetwork**: Определяет архитектуру нейронной сети, используемую для оценки Q-значений.
- **ReplayMemory**: Хранит переходы (состояние, действие, вознаграждение, следующее состояние) для воспроизведения опыта.
- **Цикл обучения**: Контролирует процесс обучения, включая управление эпизодами и отслеживание производительности.

## Требования

Убедитесь, что у вас установлены следующие пакеты:

- `torch`
- `numpy`
- `gym`
- `matplotlib`
- `deque` (часть стандартной библиотеки)

###

# Reinforcement Learning: Mountain Climbing Agent [ENG]

## Overview

This project aims to train a reinforcement learning agent to successfully navigate and climb a virtual mountain using a Deep Q-Network (DQN). The agent learns through trial and error, utilizing a replay memory to store its experiences and improve its decision-making over time.

## Project Structure

- **Agent**: Implements the core logic for selecting actions and training the DQN.
- **QNetwork**: Defines the neural network architecture used to estimate Q-values.
- **ReplayMemory**: Stores transitions (state, action, reward, next state) for experience replay.
- **Training Loop**: Controls the training process, including episode management and performance tracking.

## Requirements

Ensure you have the following packages installed:

- `torch`
- `numpy`
- `gym`
- `matplotlib`
- `deque` (part of the standard library)