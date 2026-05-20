from datetime import datetime


class ToolRegistry:
    def execute(self, tool_name, payload):
        if tool_name == "crm_update":
            return {
                "tool": tool_name,
                "status": "success",
                "message": "CRM campaign updated and stakeholder notifications generated",
                "timestamp": datetime.utcnow().isoformat(),
                "payload": payload
            }

        return {
            "tool": tool_name,
            "status": "unknown"
        }
