from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter
)

provider = TracerProvider()     
processor = BatchSpanProcessor(ConsoleSpanExporter())       # How spans are processed. Processed in batches and exported onto the console. 
provider.add_span_processor(processor)


# Sets the global default tracer provider
trace.set_tracer_provider(provider)

tracer = trace.get_tracer("my.tracer.name")

@tracer.start_as_current_span("_add")
def _add(a: int, b: int):
    return a+b

@tracer.start_as_current_span("add")
def add(a: int, b: int):
    return _add(a, b)


if __name__ == "__main__":
    return_val = add(5, 6)
    print(return_val)