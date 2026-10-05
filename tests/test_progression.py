from agentx.progression import customer_fde

def test_customer_fde_waits_for_approval():
    pending = customer_fde("highly available GCP app for 50K users with PostgreSQL and disaster recovery")
    done = customer_fde("highly available GCP app for 50K users with PostgreSQL and disaster recovery", approved=True)
    assert pending["stage"] == "customer_approval"
    assert done["applied"] is False
    assert done["proposal"]["ha"] is True

