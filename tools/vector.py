import streamlit as st
from llm import llm, embeddings
from graph import graph

from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from langchain_core.prompts import ChatPromptTemplate


from langchain.vectorstores import Neo4jVector

# Delete the existing vector index


neo4jvector = Neo4jVector.from_existing_index(
    embedding=embeddings,
    graph=graph,
    index_name="moviePlots",
    node_label="Movie",           # Ensure this label exists
    text_node_property="plot",    # Ensure this property exists
    embedding_node_property="plotEmbedding",  # Ensure this property exists
    retrieval_query="""
    RETURN
        node.plot AS text,
        score,
        {
            title: node.title,
            directors: [ (person)-[:DIRECTED]->(node) | person.name ],
            actors: [ (person)-[r:ACTED_IN]->(node) | [person.name, r.role] ],
            tmdbId: node.tmdbId,
            source: 'https://www.themoviedb.org/movie/'+ node.tmdbId
        } AS metadata
    """
)
print("Neo4jVector setup successful.")

retriever = neo4jvector.as_retriever()
print("retriever", retriever)
instructions = (
    "Use the given context to answer the question."
    "If you don't know the answer, say you don't know."
    "Context: {context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", instructions),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)

plot_retriever = create_retrieval_chain(
    retriever, 
    question_answer_chain
)

def get_movie_plot(input):
    return plot_retriever.invoke({"input": input})