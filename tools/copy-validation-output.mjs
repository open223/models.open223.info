function outputText(node) {
  const data = node.jupyter_data;
  if (data?.output_type !== "stream" || data.name !== "stdout") return "";
  return Array.isArray(data.text) ? data.text.join("") : (data.text ?? "");
}

const copyValidationOutput = {
  name: "copy-validation-output",
  doc: "Render validation stdout as a copyable text block.",
  stage: "document",
  plugin: (_, utils) => (tree) => {
    const cells = utils
      .selectAll("block", tree)
      .filter((node) => node.kind === "notebook-code");

    cells.forEach((cell) => {
      const source = cell.children?.find(
        (node) => node.type === "code" && node.executable,
      );
      if (!source?.value?.includes("ctx = model.validate()")) return;

      const outputIndex = cell.children.findIndex(
        (node) => node.type === "outputs",
      );
      if (outputIndex === -1) return;

      const output = cell.children[outputIndex];
      const text = output.children?.map(outputText).join("") ?? "";
      if (!text) return;

      // The book theme gives ordinary code blocks its native clipboard button.
      cell.children[outputIndex] = {
        type: "code",
        lang: "text",
        value: text,
        class: "validation-output",
      };
    });
  },
};

const plugin = {
  name: "Open223 validation output",
  transforms: [copyValidationOutput],
};

export default plugin;
