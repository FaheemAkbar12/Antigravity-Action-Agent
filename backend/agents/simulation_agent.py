def simulation_agent(action_result):

    return {
        "simulation_status": "SUCCESS",
        "actions_executed": [
            "CRM campaign activated",
            "Notification workflow triggered",
            "Business dashboard updated"
        ],
        "system_state_before": {
            "campaign_status": "OFF",
            "customer_churn": "12%",
            "market_health": "CRITICAL"
        },
        "system_state_after": {
            "campaign_status": "ACTIVE",
            "customer_churn": "5%",
            "market_health": "STABLE"
        },
        "execution_logs": [
            "[INFO] Connecting to CRM",
            "[INFO] Activating campaign",
            "[SUCCESS] Workflow completed"
        ]
    }