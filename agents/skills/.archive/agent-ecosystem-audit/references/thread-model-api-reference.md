# Thread/Event Model — Quick API Reference

## Core types

```python
from hermes_thread import Thread, Event, Action, ThreadStore

# Create a Thread
thread = Thread(title="Task name", agent_id="brock", system_prompt="You are...")

# Factory methods for Events
Event.user_message(agent_id, content, **meta)
Event.tool_call(agent_id, tool_name, tool_args, **meta)
Event.tool_result(agent_id, tool_name, result, parent_event_id, **meta)
Event.error(agent_id, message, tool_name, retry_count, **meta)
Event.human_approval_request(agent_id, question, context, approval_type, choices, **meta)
Event.human_response(agent_id, content, approved, **meta)
Event.done(agent_id, summary, artifacts, **meta)
Event.system(agent_id, message, **meta)
Event.handoff(from_agent, to_agent, context, artifacts, priority, **meta)

# Add events to thread
thread.add_event(event)

# Context building
context = build_context(thread)          # Full context
context = build_compact_context(thread)  # With error compaction

# Serialize
thread.save()                            # ~/.hermes/threads/<id>.json
thread = Thread.load(thread_id)          # Load from disk

# Fork
forked = thread.fork("New title", fork_at_event_index)

# Error handling
error_count = thread.consecutive_error_count()
thread, action = handle_error(thread, error_event, parent_agent)

# Pause/Resume
thread, action = pause_for_human(thread, question, agent_id)
thread, action = resume_with_human_response(thread, response, approved)

# Thread store
store = ThreadStore()
store.save(thread)
store.load(thread_id)
store.list_threads(agent_id="harry_hr", status="waiting_for_human", limit=50)
store.delete(thread_id)

# Metrics
metrics = AgentMetrics(agent_id="harry_hr", period_start=..., period_end=...)
metrics = record_metrics(metrics, thread)
```

## Handoff protocol

```python
from hermes_handoff import HandoffManager, HandoffEnvelope, quick_handoff

manager = HandoffManager()
thread, envelope = manager.create_handoff(from_thread, to_agent, summary, what_is_needed, context, artifacts, constraints, priority)
new_thread = manager.accept_handoff(envelope, system_prompt, metadata)
thread, envelope = quick_handoff(manager, template_name, from_thread, **kwargs)

# Templates: build_request, image_request, legal_review, research_pack, seo_content, incident_escalation
```

## Capability registry

```python
from hermes_registry import CapabilityRegistry, ToolAccessController

registry = CapabilityRegistry()
caps = registry.load_all()
agent = registry.get_agent("harry_hr")
ph_agents = registry.find_by_market("philippines")
table = registry.routing_table()

controller = ToolAccessController()
allowed, reason = controller.check("harry_hr", "delegate_task")  # (False, "TOOL DENIED...")
policy = controller.get_policy("harry_hr")
```

## Metrics

```python
from hermes_metrics import MetricsCollector, build_dashboard, estimate_cost

collector = MetricsCollector()
metrics = collector.collect_weekly(agent_id="harry_hr")
dashboard_path = build_dashboard(metrics, "~/Desktop/dashboard.html")

cost = estimate_cost("brock", tokens_in=5000, tokens_out=2000)
# {"agent_id": "brock", "tier": "tier_3_deep_reasoning", "cost_aud": 0.105}
```
