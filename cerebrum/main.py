import json
import os

from src.planner import CerebrumPlanner
from src.decision_maker import ConsciousDecisionMaker
from src.strategist import StrategicPlanner
from src.integrator import InformationIntegrator
from src.receiver import InputReceiver
from src.delegator import ActionDelegator
from src.filter import InformationFilter
from src.memory_manager import WorkingMemoryManager
from src.learning import LearningModule
from src.abstract_thought import AbstractThoughtProcessor
from src.reasoning import ReasoningEngine
from src.problem_solving import ProblemSolver
from src.contextualizer import Contextualizer

class Architect:
    def __init__(self):
        self.planner = CerebrumPlanner()
        self.decision_maker = ConsciousDecisionMaker()
        self.strategist = StrategicPlanner()
        self.integrator = InformationIntegrator()
        self.receiver = InputReceiver()
        self.delegator = ActionDelegator()
        self.filter = InformationFilter()
        self.memory_manager = WorkingMemoryManager()
        self.learning_module = LearningModule()
        self.abstract_thought_processor = AbstractThoughtProcessor()
        self.reasoning_engine = ReasoningEngine()
        self.problem_solver = ProblemSolver()
        self.contextualizer = Contextualizer()

        self.load_settings()

    def load_settings(self):
        with open('settings.json') as f:
            self.settings = json.load(f)

    def process_incoming_data(self, data):
        filtered_data = self.filter.prioritize(data)
        integrated_data = self.integrator.synthesize(filtered_data)
        context_data = self.contextualizer.add_context(integrated_data)
        return context_data

    def make_decision(self, data):
        context_data = self.process_incoming_data(data)
        decision = self.decision_maker.evaluate(context_data)
        return decision

    def execute_plan(self, plan):
        self.delegator.delegate(plan)

    def run(self):
        while True:
            data = self.receiver.receive()
            decision = self.make_decision(data)
            plan = self.planner.plan(decision)
            self.execute_plan(plan)

if __name__ == "__main__":
    architect = Architect()
    architect.run()
