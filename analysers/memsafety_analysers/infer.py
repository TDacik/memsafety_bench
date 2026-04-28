from benchexec import result
from benchexec.tools.template import BaseTool2
from benchexec.tools.sv_benchmarks_util import get_data_model_from_task, ILP32, LP64


class Tool(BaseTool2):
    def name(self):
        return "infer"

    def project_url(self):
        return "https://github.com/facebook/infer"

    def version(self, executable):
        return self._version_from_tool(executable)

    def executable(self, tool_locator):
        return tool_locator.find_executable("run_infer.sh")

    def cmdline(self, executable, options, task, rlimits):
        machdep = get_data_model_from_task(task, {ILP32: "-m32", LP64: "-m64"})

        return [executable, machdep, task.single_input_file]

    def determine_result(self, run):
        if run.exit_code.value != 0:
            return result.RESULT_ERROR

        if run.output.any_line_contains("error: Nullptr Dereference"):
            return result.RESULT_FALSE_DEREF

        if run.output.any_line_contains("error: Use After Free"):
            return result.RESULT_FALSE_FREE

        if run.output.any_line_contains("error: Memory Leak"):
            # Infer's memory leak does not correspond to SV-COMP mem-track
            return result.RESULT_UNKNOWN

        else:
            return result.RESULT_TRUE_PROP
