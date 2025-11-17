from datetime import date

class HealthRecord:
    """
    Represents a health record for an animal
    """
    def __init__(self, issue, severity, treatment_plan):
        self.issue = issue
        self.__date_reported = date.today()
        self.severity = severity
        self.treatment_plan = treatment_plan
        self.is_active = True  #True= Active, False= Resolved

    def get_issue(self):
        return self.__issue

    def get_date_reported(self):
        return self.__date_reported

    def get_severity(self):
        return self.__severity

    def get_treatment_plan(self):
        return self.__treatment_plan

    def get_is_active(self):
        return self.__is_active

    def set_issue(self, issue):
        if not issue or not isinstance(issue, str):
            raise ValueError("Issue is required and should be a string")
        self.__issue = issue

    def set_severity(self, severity):
        if not severity or not isinstance(severity, str):
            raise ValueError("Severity is required and should be a string")
        self.__severity = severity

    def set_treatment_plan(self, treatment_plan):
        if not treatment_plan or not isinstance(treatment_plan, str):
            raise ValueError("Treatment plan is required and should be a string")
        self.__treatment_plan = treatment_plan

    def set_is_active(self, is_active):
        if not isinstance(is_active, bool):
            raise TypeError("is_active must be a boolean (True/False).")
        self.__is_active = is_active

    issue = property(get_issue, set_issue)
    date_reported = property(get_date_reported)  # Read-only
    severity = property(get_severity, set_severity)
    treatment_plan = property(get_treatment_plan, set_treatment_plan)
    is_active = property(get_is_active, set_is_active)

