"""
Rule-Based Expert System using Forward Chaining.

This program demonstrates:
1. Knowledge Base (Rules)
2. Facts Base (User Symptoms)
3. Forward Chaining Inference
4. Multi-step Rule Chaining
5. Explanation/Reasoning Trace

Author: Ayush Kamboj
"""

class ExpertSystem:
    """
    A simple rule-based expert system that performs
    forward chaining inference on user-provided facts.
    """

    def __init__(self):
        """Initialize facts, rules, and inference log."""

        self.facts = set()
        self.inference_log = []

        self.rules = [

            # Disease Identification Rules
            ({"fever", "cough"}, "flu"),

            ({"flu", "body_pain"}, "viral_infection"),

            ({"viral_infection", "fatigue"},
             "doctor_consultation"),

            ({"doctor_consultation"},
             "seek_medical_attention"),

            ({"sneezing", "runny_nose"},
             "cold"),

            ({"cold", "headache"},
             "mild_infection"),

            ({"mild_infection"},
             "rest_and_hydration"),

            ({"fever", "rash"},
             "possible_dengue"),

            ({"possible_dengue", "joint_pain"},
             "urgent_test"),

            ({"urgent_test"},
             "doctor_consultation")
        ]

    def add_fact(self, fact):
        """
        Add a user fact (symptom) to the facts base.

        Args:
            fact (str): Symptom entered by the user.
        """
        self.facts.add(fact.lower())

    def forward_chain(self):
        """
        Execute forward chaining until no new facts
        can be inferred.
        """

        inferred = True

        while inferred:
            inferred = False

            for conditions, conclusion in self.rules:

                if (
                    conditions.issubset(self.facts)
                    and conclusion not in self.facts
                ):

                    self.facts.add(conclusion)

                    self.inference_log.append(
                        f"RULE FIRED: IF {conditions} "
                        f"THEN {conclusion}"
                    )

                    inferred = True

    def show_results(self):
        """
        Display final conclusions and reasoning trace.
        """

        print("\n" + "=" * 60)
        print("FINAL FACTS AND CONCLUSIONS")
        print("=" * 60)

        for fact in sorted(self.facts):
            print("✓", fact)

        print("\n" + "=" * 60)
        print("INFERENCE TRACE")
        print("=" * 60)

        if self.inference_log:
            for step_no, step in enumerate(
                self.inference_log,
                start=1
            ):
                print(f"{step_no}. {step}")
        else:
            print("No rules were triggered.")

        print("\n" + "=" * 60)
        print("POSSIBLE DIAGNOSIS")
        print("=" * 60)

        diagnoses = [
            "flu",
            "cold",
            "viral_infection",
            "possible_dengue"
        ]

        found = False

        for disease in diagnoses:
            if disease in self.facts:
                print("➜", disease)
                found = True

        if not found:
            print("No diagnosis determined.")

        print("=" * 60)


def main():
    """
    Main function to run the expert system.
    """

    system = ExpertSystem()

    print("=" * 60)
    print("RULE-BASED EXPERT SYSTEM")
    print("Forward Chaining Medical Diagnosis")
    print("=" * 60)

    print("\nAvailable Symptoms:")
    print("""
fever
cough
body_pain
fatigue
sneezing
runny_nose
headache
rash
joint_pain
""")

    symptoms = input(
        "\nEnter symptoms separated by commas:\n"
    )

    symptom_list = symptoms.split(",")

    for symptom in symptom_list:
        symptom = symptom.strip().lower()

        if symptom:
            system.add_fact(symptom)

    system.forward_chain()

    system.show_results()


if __name__ == "__main__":
    main()