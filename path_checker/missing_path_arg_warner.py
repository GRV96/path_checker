from .extension_possessor import ExtensionPossessor
from .path_arg_checker import PathArgChecker
from .path_checker import PathChecker


class MissingPathArgWarner(ExtensionPossessor):
	"""
	This class' main purpose is to warn the programmer that a path was not
	provided to a function or a script as an argument. If a path is given, the
	class allows to instantiate PathChecker or PathArgChecker. In order to
	work, this class needs the name of the argument that the path is the value
	of (property arg_name) and the extension that the path is supposed to have
	(property extension).
	"""

	def __init__(self, arg_name, suffixes):
		"""
		The constructor requires an argument name and a list or tuple of
		suffixes conform to the documentation of superclass
		ExtensionPossessor.

		Args:
			arg_name (str): the name of the argument that the path is the
				value of
			suffixes (list or tuple): They must make a file name extension.

		Raises:
			TypeError: if argument suffixes is not None, nor a list or a tuple
		"""
		ExtensionPossessor.__init__(self, suffixes)
		self._arg_name = arg_name

	@property
	def arg_name(self):
		"""
		This read-only property is the name of the path argument that may be
		missing.
		"""
		return self._arg_name

	def make_missing_arg_msg(self):
		"""
		The message created by this method tells that the argument named
		<argument name>, the path to a file with extension
		<expected extension>, is needed. It is relevant if the argument is
		missing.

		Returns:
			str: a message telling that the argument is needed
		"""
		return self._arg_name + ": the path to a file with extension '"\
			+ "".join(self._extension) + "' must be provided."

	def make_path_arg_checker(self, path):
		"""
		Creates a PathArgChecker instance with properties extension and
		arg_name and the given file path.

		Args:
			path (pathlib.Path or str): It should be the value of the
				path argument associated with this object.

		Returns:
			PathArgChecker: an object able to verify the path argument's value
		"""
		return PathArgChecker(path, self.extension, self.arg_name)

	def make_path_checker(self, path):
		"""
		Creates a PathChecker instance with property extension and the given
		file path.

		Args:
			path (pathlib.Path or str): It should be the value of the
				path argument associated with this object.

		Returns:
			PathChecker: an object able to verify the path argument's value
		"""
		return PathChecker(path, self.extension)
