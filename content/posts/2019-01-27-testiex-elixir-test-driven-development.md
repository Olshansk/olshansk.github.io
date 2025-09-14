---
title: "TestIex — Easier Test Driven Development in Elixir"
date: 2019-01-27T23:13:21.105Z
draft: false
description: "One of my favorite features of elixir is being able to start a shell that loads the entire context of my project:"
medium_url: "https://medium.com/@olshansky/testiex-easier-test-driven-development-in-elixir-761cd1a9f11"
tags: ["elixir", "testing", "tdd", "development", "programming"]
---

One of my favorite features of elixir is being able to start a shell that loads the entire context of my project:

```bash
$ iex -S mix
```

It provides easy access to all of the project's modules so you could easily iterate on your code by compiling it directly from within the shell. You have the option to recompile the whole project or just a single module:

```elixir
# single module
$ r MyModulesNameSpace.MyModule
```

```elixir
# whole project
$ recompile
```

The other great thing about elixir is how easy it is to run unit tests:

```bash
# all tests
$ mix test
```

```bash
# single file
$ mix test ./path/test/file/test_file_test.exs
```

```bash
# single test
$ mix test ./path/test/file/test_file_test.exs:<line_number>
```

When projects are small, *mix* makes test driven development very quick and easy. Mix also has various [test options](https://hexdocs.pm/mix/Mix.Tasks.Test.html) to optimize testing covering a lot of different use-cases. However, as the project grows, you are likely to have a lot of startup operations that may take dozens of seconds, or even minutes, to complete. It's fair to say that when an elixir application takes several minutes to start, one should identify the bottlenecks or split a single service into several microservices, but time is not a luxury we always have.

One of the things I wanted to achieve was being able to continuously iterate on my code and tests without having to wait for my whole application to start up every time. Introducing *TestIex*. This module provides an easy way to iterate on your test and source code, without ever having to exit an *iex* shell.

#### 1. Start an iex session in the test environment

```bash
$ MIX_ENV=test iex -S mix
```

#### 2. Execute the start testing command

```elixir
iex> TestIex.start_testing()
```

#### 3. Load Helpers

By default, TestIex loads the helper located under */usr/src/app/test/test_helper.exs.* Additional helpers can be loaded like so:

```elixir
iex> TestIex.load_helper("test/test_helper.exs")
```

#### 4. Run the test

```elixir
# Run a single test
iex> TestIex.test("./path/test/file/test_file_test.exs", line_number)
```

```elixir
# Run the whole test file
iex> TestIex.test("./path/test/file/test_file_test.exs")
```

```elixir
# Run multiple whole test files
iex> TestIex.test(["./path/test/file/test_file_test.exs", "./path/test/file/test_file_2_test.exs"])
```

#### 4. Iterate on test code

Test files are script files (*.exs*), which means that they do not get compiled. Modifying a test file and rerunning *TestIex.test/2* will execute the latest version of the code.

#### 5. Iterate on source code

Source code files (*.ex*) need to be recompiled every they are modified. As I've shown above, you have the option of recompiling either a single Module or the whole project depending on how many files you modified:

```elixir
# single module
$ r MyModulesNameSpace.MyModule
```

```elixir
# whole project
$ recompile
```

#### TestIex — Source Code

Here it the source code for test_iex.ex. I hope it helps you and your team in your TDD endeavors:

```elixir
defmodule TestIex do
  def start_testing() do
    ExUnit.start()
    Code.eval_file("test/test_helper.exs", File.cwd!())
    :ok
  end

  def load_helper(file_name) do
    Code.eval_file(file_name, File.cwd!())
  end

  def test(path, line \\ nil)
  def test(path, line) when is_binary(path) do
    if line do
      ExUnit.configure(exclude: [:test], include: [line: line])
    else
      ExUnit.configure(exclude: [], include: [])
    end

    Code.load_file(path)

    if v6_or_higher?() do
      ExUnit.Server.modules_loaded()
    else
      ExUnit.Server.cases_loaded()
    end

    ExUnit.run()
  end
  def test(paths, _line) when is_list(paths) do
    ExUnit.configure(exclude: [], include: [])
    Enum.map(paths, &Code.load_file/1)

    if v6_or_higher?() do
      ExUnit.Server.modules_loaded()
    else
      ExUnit.Server.cases_loaded()
    end

    ExUnit.run()
  end

  def v6_or_higher?(), do:
    if System.version() |> String.split(".") |> Enum.at(1) |> String.to_integer >= 6 do
  end
end
```