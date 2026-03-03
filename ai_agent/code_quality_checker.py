from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class CodeQualityChecker:
    def __init__(self, model_name: str = "gpt-4o-mini") -> None:
        self.llm = ChatOpenAI(model=model_name, temperature=0)
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a strict code quality reviewer."),
                ("human", "Checklist:\n{checklist}\n\nSource Code:\n{code}\n\nReturn observations per checklist item and suggested improvements."),
            ]
        )

    def review(self, source_code: str, checklist: str) -> str:
        chain = self.prompt | self.llm
        return chain.invoke({"code": source_code, "checklist": checklist}).content
