# Ronak Parikh - Rilla Take Home - July 1st, 2024

## About 
I built an Neo4j-backed Chatbot using Python to answer questions above movies / movie plots that runs in the terminal. The chatbot maintains conversation history and dynamically adjusts its response generation parameters (temeperature or randomness) based on user feedback. 



## Setup / Installation: 

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Sixfold-AI/ds-ml-challenge-ronak45.git
   cd your-repo
2. **Create a virtual environment (optional but recommended):**
   ```sh
    python3 -m venv venv
    source venv/bin/activate (On Windows use `venv\Scripts\activate`)
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
4. Change to base directory and run the app
    ```sh
    python3 dashboard/app.py
5. Update the secretws in secrets.toml and create a sandbox at https://sandbox.neo4j.com/. 
6. Within the sandbox, run the below to create a moviePlots index:
```
CREATE VECTOR INDEX moviePlots IF NOT EXISTS
FOR (m:Movie)
ON m.embedding
OPTIONS {indexConfig: {
 `vector.dimensions`: 1536,
 `vector.similarity_function`: 'cosine'
}}
```

## Usage
To run the chatbot, execute the following command in your terminal:
```
python terminal_chatbot.py
```

## Features
Session Management: Each session is assigned a unique identifier to track and manage conversations.

Dynamic Temperature Adjustment: The chatbot adjusts its response generation temperature based on recent feedback to improve response quality.

Conversation and Feedback Logging: All user inputs, bot responses, and feedback are logged for future reference and analysis.


## Logging
#### Feedback Log: Stores user feedback and related information in feedback_log.json.
#### Conversation Log: Stores the entire conversation history in conversation_log.json.

## Error Handling
The chatbot includes basic error handling to manage unexpected issues during response generation.



## Example Usage:

## 1. Tool Use with Neo4J Cypher Integration
You: What movies are Keanu Reeves in?
Bot: Thinking...

> Entering new AgentExecutor chain...
Thought: Do I need to use a tool? Yes
Action: Movie information
Action Input: "Keanu Reeves movies"

> Entering new GraphCypherQAChain chain...
Generated Cypher:
cypher
MATCH (p:Person {name: "Keanu Reeves"})-[r:ACTED_IN]->(m:Movie)
RETURN m.title

Full Context:
[{'m.title': "Something's Gotta Give"}, {'m.title': 'The Replacements'}, {'m.title': 'Johnny Mnemonic'}, {'m.title': "The Devil's Advocate"}, {'m.title': 'The Matrix Revolutions'}, {'m.title': 'The Matrix Reloaded'}, {'m.title': 'The Matrix'}]

> Finished chain.
{'query': 'Keanu Reeves movies', 'result': "Something's Gotta Give, The Replacements, Johnny Mnemonic, The Devil's Advocate, The Matrix Revolutions, The Matrix Reloaded, The Matrix"}Final Answer: Keanu Reeves has appeared in several notable movies, including:

1. **Something's Gotta Give**
2. **The Replacements**
3. **Johnny Mnemonic**
4. **The Devil's Advocate**
5. **The Matrix Revolutions**
6. **The Matrix Reloaded**
7. **The Matrix**

If you need more information about any specific movie or other movies he has been in, feel free to ask!

> Finished chain.
Bot: Keanu Reeves has appeared in several notable movies, including:

1. **Something's Gotta Give**
2. **The Replacements**
3. **Johnny Mnemonic**
4. **The Devil's Advocate**
5. **The Matrix Revolutions**
6. **The Matrix Reloaded**
7. **The Matrix**

If you need more information about any specific movie or other movies he has been in, feel free to ask!
Was this response helpful? (positive/negative): positive

## Showing feedback loop here

Current Temperature: 0.70

## Showing conversation history here...
You: What is the plot of the last movie you listed above? 
Bot: Thinking...


> Entering new AgentExecutor chain...
Thought: Do I need to use a tool? Yes
Action: Movie Plot Search
Action Input: The Matrix

{'input': 'The Matrix\n', 'context': [], 'answer': '"The Matrix" is a science fiction film released in 1999, directed by the Wachowskis. The story follows a computer hacker named Neo (played by Keanu Reeves) who discovers that the reality he lives in is actually a simulated reality created by intelligent machines to subdue the human population, while their bodies\' heat and electrical activity are used as an energy source. Neo joins a group of rebels led by Morpheus (played by Laurence Fishburne) and Trinity (played by Carrie-Anne Moss) to fight against the machines and seek the truth about the Matrix. The film is known for its groundbreaking special effects, including the innovative use of "bullet time" slow-motion photography, and its exploration of philosophical and existential themes.'}Final Answer: "The Matrix" is a science fiction film released in 1999, directed by the Wachowskis. The story follows a computer hacker named Neo (played by Keanu Reeves) who discovers that the reality he lives in is actually a simulated reality created by intelligent machines to subdue the human population, while their bodies' heat and electrical activity are used as an energy source. Neo joins a group of rebels led by Morpheus (played by Laurence Fishburne) and Trinity (played by Carrie-Anne Moss) to fight against the machines and seek the truth about the Matrix. The film is known for its groundbreaking special effects, including the innovative use of "bullet time" slow-motion photography, and its exploration of philosophical and existential themes.

> Finished chain.
Bot: "The Matrix" is a science fiction film released in 1999, directed by the Wachowskis. The story follows a computer hacker named Neo (played by Keanu Reeves) who discovers that the reality he lives in is actually a simulated reality created by intelligent machines to subdue the human population, while their bodies' heat and electrical activity are used as an energy source. Neo joins a group of rebels led by Morpheus (played by Laurence Fishburne) and Trinity (played by Carrie-Anne Moss) to fight against the machines and seek the truth about the Matrix. The film is known for its groundbreaking special effects, including the innovative use of "bullet time" slow-motion photography, and its exploration of philosophical and existential themes.
Was this response helpful? (positive/negative): positive

Current Temperature: 0.60

{'query': 'Gal Gadot movies', 'result': "I don't know the answer."}Thought: I should try another tool to find information about movies featuring Gal Gadot.

Action: General Chat
Action Input: "What movies are Gal Gadot in?"Gal Gadot is an Israeli actress and model who has appeared in numerous films. Some of her notable movie roles include:

1. **"Fast & Furious" series**:
   - "Fast & Furious" (2009)
   - "Fast Five" (2011)
   - "Fast & Furious 6" (2013)

2. **DC Extended Universe (DCEU)**:
   - "Batman v Superman: Dawn of Justice" (2016) as Wonder Woman
   - "Wonder Woman" (2017) as the title character
   - "Justice League" (2017) as Wonder Woman
   - "Wonder Woman 1984" (2020) as the title character
   - "Zack Snyder's Justice League" (2021) as Wonder Woman

3. **Other Films**:
   - "Keeping Up with the Joneses" (2016)
   - "Triple 9" (2016)
   - "Criminal" (2016)
   - "Ralph Breaks the Internet" (2018) — voice role
   - "Red Notice" (2021)
   - "Death on the Nile" (2022)
   
This list includes some of her most prominent roles, but she has also appeared in other projects and continues to be active in the industry.An error occurred: An output parsing error occurred. In order to pass this error back to the agent and have it try again, pass `handle_parsing_errors=True` to the AgentExecutor. This is the error: Could not parse LLM output: `Gal Gadot is an Israeli actress and model who has appeared in numerous films. Some of her notable movie roles include:

1. **"Fast & Furious" series**:
   - "Fast & Furious" (2009)
   - "Fast Five" (2011)
   - "Fast & Furious 6" (2013)

2. **DC Extended Universe (DCEU)**:
   - "Batman v Superman: Dawn of Justice" (2016) as Wonder Woman
   - "Wonder Woman" (2017) as the title character
   - "Justice League" (2017) as Wonder Woman
   - "Wonder Woman 1984" (2020) as the title character
   - "Zack Snyder's Justice League" (2021) as Wonder Woman

3. **Other Films**:
   - "Keeping Up with the Joneses" (2016)
   - "Triple 9" (2016)
   - "Criminal" (2016)
   - "Ralph Breaks the Internet" (2018) — voice role
   - "Red Notice" (2021)
   - "Death on the Nile" (2022)
   
This list includes some of her most prominent roles, but she has also appeared in other projects and continues to be active in the industry.`


3. ### General Chat Use

You: What movies are gal gadot in?
Bot: Thinking...

> Entering new AgentExecutor chain...
Thought: Do I need to use a tool? Yes
Action: Movie information
Action Input: "Gal Gadot movies"

> Entering new GraphCypherQAChain chain...
Generated Cypher:
cypher
MATCH (p:Person {name: "Gal Gadot"})-[r:ACTED_IN]->(m:Movie)
RETURN m.title

### Not found in the db...
Full Context:
[] 

> Finished chain.
{'query': 'Gal Gadot movies', 'result': "I don't know the answer."}Thought: I should try another tool to find information about movies featuring Gal Gadot.

Action: General Chat
Action Input: "What movies are Gal Gadot in?"Gal Gadot is an Israeli actress and model who has appeared in numerous films. Some of her notable movie roles include:

1. **"Fast & Furious" series**:
   - "Fast & Furious" (2009)
   - "Fast Five" (2011)
   - "Fast & Furious 6" (2013)

2. **DC Extended Universe (DCEU)**:
   - "Batman v Superman: Dawn of Justice" (2016) as Wonder Woman
   - "Wonder Woman" (2017) as the title character
   - "Justice League" (2017) as Wonder Woman
   - "Wonder Woman 1984" (2020) as the title character
   - "Zack Snyder's Justice League" (2021) as Wonder Woman

3. **Other Films**:
   - "Keeping Up with the Joneses" (2016)
   - "Triple 9" (2016)
   - "Criminal" (2016)
   - "Ralph Breaks the Internet" (2018) — voice role
   - "Red Notice" (2021)
   - "Death on the Nile" (2022)
