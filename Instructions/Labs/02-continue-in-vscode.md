---
lab:
  title: Continue developing your agent in Visual Studio Code
  description: Use Visual Studio Code to develop and test your agent.
  level: 200
  duration: 20 minutes
  islab: true
---

# Continue developing your agent in Visual Studio Code

In the **[previous exercise](./01-get-started-in-foundry.md)**, you used Microsoft Foundry to start developing an AI agent that provides information and expertise on the history of computing.

Now you're ready to continue developing your agent using the Foundry integration features of Visual Studio Code.

This exercise should take approximately **20** minutes to complete.

## Install the Foundry Toolkit extension for Visual Studio Code

The Foundry Toolkit extension for Visual Studio Code brings the assets in your Foundry projects right into the development environment.

1. Start Visual Studio Code
1. In the navigation bar on the left, view the **Extensions** page.
1. Search the extensions marketplace for `Foundry Toolkit`, and install the **Foundry Toolkit for VS Code** extension.

    The extension may take a minute or so to install.

1. After installing the extension, select the **Foundry Toolkit** page in the left navigation bar; and wait for it to load.

    ![Screenshot of the Foundry Toolkit Visual Studio Code extension.](./media/foundry-vs-extension.png)

1. In the Foundry Toolkit pane, expand **My Resources** and set the default project by connecting to Azure (signing in with your credentials) and selecting the Foundry project you created previously.

    > **Tip**: If you did not complete the previous exercise, use the extension to sign into Azure and create a new project.

## Connect to your agent

Now that you have a connection to your Foundry project, you can access the assets you've created in it - including the *computing-historian* agent you created in the previous exercise.

> **Tip**: If you didn't complete the previous exercise, or have deleted your *computing-history* agent, use the **+** icon for the **Prompt agents** node to create a new agent named `computing-history` based on the *gpt-5-mini* model with the instructions `You are an expert in the history of computing and AI.` and add the *Web search* tool.

1. In the Foundry Toolkit pane, under your project, select **Agents** and on the **Prompt agents** tab, select the **computing-historian** agent you created previously.

    The latest version of the agent is opened in the **Agent Builder** interface within Visual Studio Code, so you can continue to develop and test it.

    ![Screenshot of the Agent Builder in Visual Studio Code.](./media/vs-code-playground.png)

## Write code to test your agent

While you can use the graphical interface in the Foundry Portal and the Foundry Extension in Visual Studio code to develop and test an agent, eventually you'll want to write and test code. You can use the Azure AI Projects SDK and the OpenAI Responses API to do so.

1. In the **Agent Builder** pane, and select **View code**. Then when prompted, browse to the location on your local drive where you want to store your agent code.

    A new Visual Studio Code instance is opened, containing code files to work with your agent.

1. In the new Visual Studio Code workspace, select the **run_agent.py** code file. The code it contains should look similar to this:

    ```python
    """Build Agent using Microsoft Agent Framework in Python
    
    # Run this python script
    >
    > pip install agent-framework==1.0.0rc6
    > python <this-script-path>.py
    """
    
    import asyncio
    import os
    from dotenv import load_dotenv
    
    from agent_framework_foundry import FoundryAgent
    from azure.identity.aio import DefaultAzureCredential
    
    load_dotenv()
    
    # User inputs for the conversation
    
    USER_INPUTS = [
        "Hello",
    ]
    
    async def main() -> None:
        # For authentication, DefaultAzureCredential supports multiple authentication methods. Run `az login` in terminal for Azure CLI auth.
        async with FoundryAgent(
            project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
            agent_name="computing-historian",
            agent_version="1",
            credential=DefaultAzureCredential(),
        ) as agent:
    
            # Process user messages
            for user_input in USER_INPUTS:
                print(f"\n# User: '{user_input}'")
                printed_tool_calls = set()
                async for chunk in agent.run(user_input, stream=True):
                    # log tool calls if any
                    function_calls = [
                        c for c in chunk.contents
                        if c.type == "function_call"
                    ]
                    for call in function_calls:
                        if call.call_id not in printed_tool_calls:
                            print(f"Tool calls: {call.name}")
                            printed_tool_calls.add(call.call_id)
                    if chunk.text:
                        print(chunk.text, end="", flush=True)
                print("")
    
            print("\n--- All tasks completed successfully ---")
    
    if **name** == "**main**":
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print("\nProgram interrupted by user")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            import traceback
            traceback.print_exc()
        finally:
            print("Program finished.")
    ```

    Note the comments at the top of the file, which provide instructions for preparing the Python environment and running the script.

1. On the **Extensions** page, if it is not already installed, install the **Python** extension. Then, in the **Command Palette (Ctrl+Shift+P)**, use the command `python:create environment` (or `python:select interpreter`) to create a new *Venv* environment based on your Python 3.1x installation.

    > **Tip**: You can choose to install the workspace dependencies in the *requirements.txt* file as you create the environment. Don't worry of you accidentally skip this though; we'll do it in a later step anyway.

    When you have created the Python environment, a folder mamed **.venv** will be added to the workspace (not to be confused with the *.env* file, which contains environment variables for the program)

1. In the **Explorer** pane, right-click the **run_agent.py** file, and select **Open in integrated terminal**.

    > **Note**: Opening the terminal in Visual Studio Code should automatically activate the Python environment after a few seconds. If you're using a PowerShell terminal, you may need to enable running scripts on your system (see [Set-ExecutionPolicy](https://learn.microsoft.com/powershell/module/microsoft.powershell.security/set-executionpolicy){:target="_blank"}). If for any reason the Python environment is not activated automatically, you can use [this query](https://www.bing.com/search?q=%22How%20do%20I%20activate%20a%20Python%20venv%22){:target="_blank"} to search for information on how to activate it in your environment.

1. Ensure that the terminal is open in the **computinghistorian** folder with the prefix **(.venv)** to indicate that the Python environment you created is active.

    > **Tip**: You can enter the command `cls` to clear the console pane - which may make it easier to focus on the outputs from commands as you run them.

1. Install the required dependencies by running the following command:

    ```bash
   pip install agent-framework==1.10.0
    ```

    **Nte**: This may be a different version from the one referenced in the same code and requirements.txt file.

1. After the libraries are installed (which may take a minute or so), use the following command to sign into Azure.

    ```bash
   az login
    ```

    > **Note**: In most scenarios, just using *az login* will be sufficient. However, if you have subscriptions in multiple tenants, you may need to specify the tenant by using the *--tenant* parameter. See [Sign into Azure interactively using the Azure CLI](https://learn.microsoft.com/cli/azure/authenticate-azure-cli-interactively) for details.

1. When prompted, follow the instructions to sign into Azure. Then complete the sign in process in the command line, viewing (and confirming if necessary) the details of the subscription containing your Foundry resource.
1. After you have signed in, enter the following command to run the application:

    ```bash
   python run_agent.py
    ```

    The code should run in the terminal, submit the user prompt "*Hello*" to your agent, and display the response (if not, resolve any errors and try again).

    ![Screenshot of a terminal with code output in Visual Studio Code.](./media/vs-code-run-agent.png)

## Use GitHub Copilot to expand your code

GitHub Copilot provides agentic AI assistance in Visual Studio Code, helping you develop applications more efficiently.

> **Note**: GitHub Copilot in Visual Studio Code requires that you are signed in using a GitHub account. While agentic assistance is available in all GitHub plans, including free accounts, there are usage limitations.

1. In Visual Studio Code, in the **Extensions** pane, ensure that the **GitHub Copilot Chat** extension is installed and enabled.
1. At the bottom of the activity bar on the left, select **Accounts** and ensure that you are signed into your GitHub account. If not, sign in to use AI features.
1. On the toolbar, next to the search box, use the **Toggle Chat** button to show the chat pane on the right.

    ![Screenshot of GitHub Copilot in Visual Studio Code.](./media/vscode-github-copilot.png)

    The **Chat** pane is where you configure and use GitHub Copilot and connected agents to assist you with development tasks. You can select the model that GitHub Copilot uses, configure tools, and add custom agents. We'll use the default settings in this exercise.

1. Ensure the **agent.py** code file is open in the editor, then in the **Chat** pane, enter the following prompt:

    ```
    Modify the code to iteratively ask the user to enter a prompt for the agent and display the results, running until the user enters "quit". 
    ```

1. Enter the prompt, and wait while GitHub Copilot reviews and modifies your code. Eventually the changes will be staged and displayed.

    ![Screenshot of GitHub Copilot in Visual Studio Code.](./media/vscode-modified-code.png)

1. With the changes staged, in the terminal, re-run the code (`python agent.py`).

    This time the app should continually ask you to enter a prompt and display the results until you enter "quit". (if not, continue to iterate with GitHub Copilot in the chat pane, explaining the behavior you want and any errors that occur until the code works as expected.)

    Some suggested prompts to try:

    - `Tell me about the Commodore 64`
    - `What was the ZX Spectrum?`
    - `What was Grace Hopper's contribution to computing?`

    When you're finished, enter `quit`.

1. If you're happy with the code that GitHub Copilot has generated, use the **Keep** button in the **Chat** pane to confirm the changes.

## Summary

In this exercise, you used the Foundry Toolkit extension in Visual Studio Code and the Agent Framework to develop an agentic solution. You also used GitHub Copilot to get agentic AI assistance when developing your solution.

## Next steps

This is the second in a series of lab exercises; save your work and continue to the **[next exercise](./03-use-agent.md)** if you're ready.

> **Tip**: If you do not plan to complete the next exercise, you should delete the Azure resources created in this exercise to avoid unnecessary utilization charges.
