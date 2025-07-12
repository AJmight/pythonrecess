import numpy as np
import random

# Define the states and actions
states = ['start', 'look_left', 'look_right', 'look_left_again', 'cross', 'safe', 'hit']
actions = ['look_left', 'look_right', 'cross']

# Initialize Q-table with zeros
q_table = np.zeros((len(states), len(actions)))

# Learning parameters
alpha = 0.1  # Learning rate
gamma = 0.6  # Discount factor
epsilon = 0.1  # Exploration rate

# Reward system
rewards = {
    ('start', 'look_left'): 1,
    ('look_left', 'look_right'): 1,
    ('look_right', 'look_left_again'): 1,
    ('look_left_again', 'cross'): 10,  # Big reward for correct sequence
    ('cross', 'safe'): 50,  # Successfully crossed
    ('cross', 'hit'): -100  # Got hit by car
}

# Training function
def train(num_episodes):
    for episode in range(num_episodes):
        state = 'start'
        sequence = []
        
        while state not in ['safe', 'hit']:
            # Epsilon-greedy action selection
            if random.uniform(0, 1) < epsilon:
                action = random.choice(actions)  # Explore
            else:
                state_idx = states.index(state)
                action_idx = np.argmax(q_table[state_idx])
                action = actions[action_idx]  # Exploit
            
            sequence.append((state, action))
            
            # Determine next state and reward
            if state == 'start' and action == 'look_left':
                next_state = 'look_left'
                reward = rewards.get((state, action), 0)
            elif state == 'look_left' and action == 'look_right':
                next_state = 'look_right'
                reward = rewards.get((state, action), 0)
            elif state == 'look_right' and action == 'look_left_again':
                next_state = 'look_left_again'
                reward = rewards.get((state, action), 0)
            elif state == 'look_left_again' and action == 'cross':
                # 90% chance of crossing safely if following the correct sequence
                if random.random() < 0.9:
                    next_state = 'safe'
                else:
                    next_state = 'hit'
                reward = rewards.get((state, action), 0)
            else:
                # Wrong action sequence - likely to get hit
                if random.random() < 0.7:
                    next_state = 'hit'
                else:
                    next_state = random.choice(states)
                reward = -10
            
            # Q-learning update
            state_idx = states.index(state)
            next_state_idx = states.index(next_state)
            action_idx = actions.index(action)
            
            old_value = q_table[state_idx, action_idx]
            next_max = np.max(q_table[next_state_idx])
            
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state_idx, action_idx] = new_value
            
            state = next_state
        
        # Print progress
        if episode % 100 == 0:
            print(f"Episode: {episode}, Final state: {state}, Sequence: {sequence}")

# Test the trained model
def test():
    state = 'start'
    sequence = []
    
    print("Testing the trained model:")
    while state not in ['safe', 'hit']:
        state_idx = states.index(state)
        action_idx = np.argmax(q_table[state_idx])
        action = actions[action_idx]
        
        sequence.append((state, action))
        
        # Simulate state transition
        if state == 'start' and action == 'look_left':
            next_state = 'look_left'
        elif state == 'look_left' and action == 'look_right':
            next_state = 'look_right'
        elif state == 'look_right' and action == 'look_left_again':
            next_state = 'look_left_again'
        elif state == 'look_left_again' and action == 'cross':
            next_state = 'safe'  # Assume success in test
        else:
            next_state = 'hit'
        
        state = next_state
    
    print("Sequence executed:")
    for step in sequence:
        print(f"- {step[0]}: {step[1]}")
    print(f"Final result: {state}")

# Train the model
train(1000)

# Test the model
test()

# Show the learned Q-table
print("\nLearned Q-table:")
print(q_table)