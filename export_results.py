from basic_types import Problem
from utils import print_, print_sec, print_ssec


def export_results(prob: Problem, outfile: str):
    """Export the results to the file specified."""

    print_ssec("Exporting results to {}".format(outfile))

    out_lines = []
    for a in prob.assigns:
        with open(outfile, 'w') as f_out:
            msg = "{} {}\n".format(len(a), " ".join([str(i.id) for i in a]))
            out_lines.append(msg)
            f_out.writelines(out_lines)
    print_("Exported.")
