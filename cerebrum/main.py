import json
import os

from src.planner import SeCuReDmE_systemPlanner
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

from src.visionary.holistic_analysis import HolisticAnalysis
from src.visionary.spatial_mapping import SpatialMappingAndNavigation
from src.visionary.gestalt_pattern_matching import GestaltPatternMatching
from src.visionary.creative_generation import CreativeGeneration
from src.visionary.non_verbal_signal_processing import NonVerbalSignalProcessing
from src.visionary.intuitive_reasoning import IntuitiveReasoning

class Architect:
    def __init__(self):
        self.planner = SeCuReDmE_systemPlanner()
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

        self.holistic_analysis = HolisticAnalysis()
        self.spatial_mapping = SpatialMappingAndNavigation()
        self.gestalt_pattern_matching = GestaltPatternMatching()
        self.creative_generation = CreativeGeneration()
        self.non_verbal_signal_processing = NonVerbalSignalProcessing()
        self.intuitive_reasoning = IntuitiveReasoning()

        self.load_settings()

    def load_settings(self):
        with open('settings.json') as f:
            self.settings = json.load(f)

    def process_incoming_data(self, data):
        filtered_data = self.filter.prioritize(data)
        integrated_data = self.integrator.synthesize(filtered_data)
        context_data = self.contextualizer.add_context(integrated_data)

        holistic_context = self.holistic_analysis.process_information(context_data)
        spatial_context = self.spatial_mapping.process_spatial_data(context_data)
        pattern_context = self.gestalt_pattern_matching.identify_patterns(context_data)
        creative_context = self.creative_generation.generate_ideas(context_data)
        non_verbal_context = self.non_verbal_signal_processing.process_signals(context_data)
        intuitive_context = self.intuitive_reasoning.generate_insights(context_data)

        combined_context = {
            "holistic": holistic_context,
            "spatial": spatial_context,
            "patterns": pattern_context,
            "creative": creative_context,
            "non_verbal": non_verbal_context,
            "intuitive": intuitive_context
        }

        return combined_context

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
