Ronak Parikh - Rilla Take Home -

I built an Neo4j-backed Chatbot using Python to answer questions above movies / movie plots.

Setup / Installation: 



```
CREATE VECTOR INDEX moviePlots IF NOT EXISTS
FOR (m:Movie)
ON m.embedding
OPTIONS {indexConfig: {
 `vector.dimensions`: 1536,
 `vector.similarity_function`: 'cosine'
}}
```

Example Usage:

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

# Showing feedback loop here

Current Temperature: 0.70

# Showing conversation history here...
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

# rilla_submission
