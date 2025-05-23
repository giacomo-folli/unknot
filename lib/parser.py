class Parser:
    _mantra_templ_str = "%mantra%"
    _prompt_templ_str = "%prompt%"
    _theme_templ_str = "%theme%"
    _free_templ_str = f"%free%"
    _num_templ_str = "%num%"

    def __init__(
        self,
        template_path: str,
        mantra: str,
        prompt: str,
        theme: str,
        free: str,
        num: str,
    ):
        with open(template_path, "r") as f:
            self._content = f.read()

        self._mantra = mantra
        self._prompt = prompt
        self._theme = theme
        self._free = free
        self._num = num

    def set_mantra(self, mantra):
        self._content = self._content.replace(self._mantra_templ_str, mantra)

    def set_free(self, free):
        self._content = self._content.replace(self._free_templ_str, free)

    def set_prompt(self, prompt):
        self._content = self._content.replace(self._prompt_templ_str, prompt)

    def set_theme(self, theme):
        self._content = self._content.replace(self._theme_templ_str, theme)

    def set_num(self, num):
        self._content = self._content.replace(self._num_templ_str, num)

    def parse(self):
        self.set_mantra(self._mantra)
        self.set_prompt(self._prompt)
        self.set_theme(self._theme)
        self.set_free(self._free)
        self.set_num(self._num)
        return self._content
